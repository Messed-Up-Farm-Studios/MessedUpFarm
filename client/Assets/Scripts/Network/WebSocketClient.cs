using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Models.Messages;
using UnityEngine;



public class WebSocketClient : MonoBehaviour
{

    public static WebSocketClient Instance;
    private ClientWebSocket ws;
    private CancellationTokenSource cts;    

    private MessageRouter router = new MessageRouter();
    
    void Awake()
    {
        Instance = this;
    }


    public async Task Connect(string url)
    {
        ws = new ClientWebSocket();
        cts = new CancellationTokenSource();

        try
        {
        await ws.ConnectAsync(new Uri(url), cts.Token);
        Debug.Log("WebSocket Connected");
        _ = ReceiveLoop();
        } 
        catch (Exception e)
        {
        Debug.Log("WebSocket Connection Failed: " + e.Message);
        }

    }

    public async Task Send(string message)
    {
        if (ws == null || ws.State != WebSocketState.Open) return;

        byte[] bytes = Encoding.UTF8.GetBytes(message);

        await ws.SendAsync(
            new ArraySegment<byte>(bytes),
            WebSocketMessageType.Text,
            true,
            cts.Token
        );
    }

    private async Task ReceiveLoop()
    {
        byte[] buffer = new byte[1024];

        try
        {
            while (ws != null && ws.State == WebSocketState.Open)
            {
                var result = await ws.ReceiveAsync(
                new ArraySegment<byte>(buffer),
                cts.Token
                );

                if (result.MessageType == WebSocketMessageType.Close)
                {   
                    Debug.Log("Server inititated close: " + result.CloseStatus);   
                    router.Route(NetworkMessageFactory.Error("Server inititated close: " + result.CloseStatus));

                    await SafeClose();
                    break;
                }

                string msg = Encoding.UTF8.GetString(buffer, 0, result.Count);
                router.Route(msg);
            }
        }
        catch (WebSocketException  e)
        {
            Debug.LogWarning("WebSocketClient disconnected: " + e.Message);
            router.Route(NetworkMessageFactory.Error("WebSocketClient disconnected: " + e.Message));

        }
        catch (OperationCanceledException e) 
        {
            Debug.Log("WebSocket receive cancelled." + e.Message);
        } 
        catch (Exception e)
        {
            Debug.LogError("Unexpected WebSocket error: " + e.Message);
            router.Route(NetworkMessageFactory.Error("Unexpected WebSocket error: " + e.Message));
        }
        finally
        {
            await SafeClose();
        }
    }


    private async Task SafeClose()
    {
        if (ws == null) return;

        try
        {
            if (ws.State == WebSocketState.Open || ws.State == WebSocketState.CloseReceived)
            {
                await ws.CloseAsync(WebSocketCloseStatus.NormalClosure,
                    "Client closing",
                    CancellationToken.None);
            }    
        }
        catch (Exception e)
        {
            Debug.LogWarning("Close error ignored: " + e.Message);
            router.Route(NetworkMessageFactory.Error("Close error ignored: " + e.Message));
        }
            
        cts?.Cancel();
        ws.Dispose(); 
        ws = null;

        }    
}