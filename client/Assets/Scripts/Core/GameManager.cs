using System;
using UnityEngine;
using Models.Messages;
using System.Threading.Tasks;
public class GameManager : MonoBehaviour
{
    public static GameManager Instance;

    public GameState CurrentState { get; private set;}        
    public GameSession Session = new GameSession();


    public event System.Action<GameState> OnStateChanged;

    private void Awake()
    {
        Instance = this;
    }

    public void Initialize()
    {
        SetState(GameState.Splash);
    }

    public void SetState(GameState newState)
    {
        if (CurrentState == newState) return;
        
        Debug.Log($"State change: {CurrentState} -> {newState}");

        CurrentState = newState;

        MainThreadDispatcher.Enqueue(() =>
        {   
            OnStateChanged?.Invoke(CurrentState);
        });

    }

    public async Task ConnectToServer()
    {
        try
        {
            SetState(GameState.Connecting);

            Debug.Log("Contacting server ...");

            await WebSocketClient.Instance.Connect("ws://127.0.0.1:8000/ws");

            SetState(GameState.MainMenu);
        }
        catch (Exception e)
        {
            HandleError(e.Message);
        }
    }

    public async Task StartMatchmaking()
    {
        SetState(GameState.Matchmaking);

        string playerID = System.Guid.NewGuid().ToString();

        FindMatchMessage findMatchMessage = new FindMatchMessage
        {
            type = "find_match",
            playerID = playerID
        };

        string json = JsonUtility.ToJson(findMatchMessage);

        await WebSocketClient.Instance.Send(json);
    }

    public void HandleMatchFound()
    {
        SetState(GameState.LoadingMatch);
    }

    public void HandleError(string errorMessage)
    {
        Session.LastError = errorMessage;

        SetState(GameState.Error);            
    }
}