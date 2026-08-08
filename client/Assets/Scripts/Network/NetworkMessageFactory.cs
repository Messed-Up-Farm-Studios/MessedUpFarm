using UnityEngine;
using Models.Messages; 

public static class NetworkMessageFactory
{
    public static string Error(string message)
    {
        return JsonUtility.ToJson(new ErrorMessage
        {
           type = "error", 
           message = message
        });
    }
}