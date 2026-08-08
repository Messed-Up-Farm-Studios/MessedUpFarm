using UnityEngine;
using System.Collections;
using System.Threading.Tasks;
using UnityEngine.SceneManagement;

public class MainMenuController : MonoBehaviour
{

    public void OnStartGamePressed()
    {
        StartMatchmakingAsync();
    }

    private async void StartMatchmakingAsync()
    {
        if (GameManager.Instance == null)
        {
            Debug.LogError("GameManager not ready yet");
        }
        
        await GameManager.Instance.StartMatchmaking();
    }

    public void ViewCredits()
    {
        SceneManager.LoadScene("Credits");
    }
}
