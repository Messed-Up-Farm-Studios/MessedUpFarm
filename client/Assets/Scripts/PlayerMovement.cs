using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerMovement : MonoBehaviour
{

    [SerializeField] private float speed = 5f;

    private Vector2 moveInput;

    public void OnMove(InputValue value)
    {   
        moveInput = value.Get<Vector2>();
    }

    void Update()
    {

        Vector3 movement = new Vector3(moveInput.x, moveInput.y, 0f);

        if (movement != Vector3.zero)
        {
            float angle = Mathf.Atan2(movement.y, movement.x) * Mathf.Rad2Deg;
            transform.rotation = Quaternion.Euler(0f, 0f, angle);            
        }
        
        transform.Translate(movement * speed * Time.deltaTime);
    }
}
