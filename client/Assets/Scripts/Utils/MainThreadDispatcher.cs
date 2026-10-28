using System;
using System.Collections.Generic;
using UnityEngine;

public class MainThreadDispatcher : MonoBehaviour
{
    public static MainThreadDispatcher Instance;

    private readonly Queue<Action> actions = new Queue<Action>();
    private static readonly object queueLock = new object();

    private void Awake()
    {
        Instance = this;
    }

    public static void Enqueue(Action action)
    {
        if (action == null) return;

        lock (queueLock)
        {
            Instance.actions.Enqueue(action);
        }
    }

    public void Update()
    {
        while (true)
        {
            Action action = null;

            lock (queueLock)
            {
                if (actions.Count > 0)
                {
                    action = actions.Dequeue();
                }
                else
                {
                    break;
                }
            }
                
            action?.Invoke();

        }
    }
}