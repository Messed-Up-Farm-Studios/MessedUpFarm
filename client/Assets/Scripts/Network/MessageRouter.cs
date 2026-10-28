using UnityEngine;
using Models.Messages;

public class MessageRouter
{
    public void Route(string msg)
    {
        var data = JsonUtility.FromJson<Message>(msg);

        if (data == null) return;
            
        switch (data.type)
        {   
            case "match_found":
            GameManager.Instance.HandleMatchFound();
            break;

            case "error":
            HandleError(msg);
            break;
        }
    }

    public void HandleError(string msg)
    {
        var errorData = JsonUtility.FromJson<ErrorMessage>(msg);

        GameManager.Instance.HandleError(errorData.message);        
    }

}