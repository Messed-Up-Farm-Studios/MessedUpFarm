using UnityEngine;

public class CreditsTextScroller : MonoBehaviour
{

    [SerializeField] private float speed = 10.0f;

    // Update is called once per frame
    void Update()
    {
        transform.Translate(Vector3.up * speed * Time.deltaTime);
    }
}
