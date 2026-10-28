using UnityEngine.SceneManagement;
using UnityEngine;

public class SplashScreenController : MonoBehaviour
{
    private async void Start()
    {
        await GameManager.Instance.ConnectToServer();
    }
}