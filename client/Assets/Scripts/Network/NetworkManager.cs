using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public partial class NetworkManager : MonoBehaviour
{
    public static NetworkManager Instance;

    public string serverResult;

    void Awake()
    {
        Instance = this;
    }

    // public IEnumerator FindMatch(string playerID)
    // {
    //     string url = "http://127.0.0.1:8000/find-match";


    //     yield return PostRequest(url, json);
    // }

    // public IEnumerator PostRequest(string url, string jsonData)
    // {
    //     UnityWebRequest request = new UnityWebRequest(url, "POST");

    //     byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonData);

    //     request.uploadHandler = new UploadHandlerRaw(bodyRaw);
    //     request.downloadHandler = new DownloadHandlerBuffer();

    //     request.SetRequestHeader("Content-Type", "application/json");

    //     yield return request.SendWebRequest();
        
    //     if (request.result == UnityWebRequest.Result.Success)
    //     {
    //         MatchResponse response = JsonUtility.FromJson<MatchResponse>(request.downloadHandler.text);
    //         Debug.Log("MatchID: " + response.matchID);
    //     }
    //     else
    //     {
    //         Debug.LogError("Error: " + request.error);
    //     }
        
    // }
}
