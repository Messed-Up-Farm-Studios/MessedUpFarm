using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;

public class NavigationController : MonoBehaviour
{
    private IEnumerator Start()
    {
        while (GameManager.Instance == null)
            yield return null;
        
        GameManager.Instance.OnStateChanged += HandleStateChanged;  
        HandleStateChanged(GameManager.Instance.CurrentState);
    }

    public void LoadScene(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }

    private void HandleStateChanged(GameState gameState)
    {

        switch (gameState)
        {
            case GameState.Splash:
                LoadScene("SplashScreen");
                break;

            case GameState.Connecting:
                LoadScene("LoadingScreen");
                break;
                
            case GameState.MainMenu:
                LoadScene("MainMenu");
                break;
            
            case GameState.Matchmaking:
                LoadScene("LoadingScreen");
                break;

            case GameState.LoadingMatch:
                LoadScene("MainMenu");
                break;

            case GameState.Error:
                LoadScene("ErrorScreen");
                break;    
        }
    }
}
