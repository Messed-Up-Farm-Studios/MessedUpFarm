using UnityEngine;
using TMPro;

public class ErrorMessageController : MonoBehaviour
{

    public TextMeshProUGUI errorMessageText;

    private void Start()
    {
        errorMessageText.text = GameManager.Instance.Session.LastError;
    }
}

