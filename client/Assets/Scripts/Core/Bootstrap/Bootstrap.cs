using UnityEngine;

public class Bootstrap : MonoBehaviour
{

    [SerializeField] private GameManager gameManager;
    private void Awake()
    {
        DontDestroyOnLoad(gameObject);

        InitializeSystems();
    }

    private void InitializeSystems()
    {
        gameManager.Initialize();
    }

}
