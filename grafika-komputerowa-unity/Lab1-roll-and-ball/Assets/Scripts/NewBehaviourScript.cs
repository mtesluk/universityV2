using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public float speed;
    private int count;
    public GameObject text; 

    // Start is called before the first frame update
    void Start()
    {
        count = 0;
    }

    // Update is called once per frame
    void Update()
    {
        float moveHor = Input.GetAxis("Horizontal");
        float moveVer = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(moveHor, 0.0f, moveVer);
        GetComponent<Rigidbody>().AddForce(movement * speed * Time.deltaTime);

        if (count >= 10) {
            text.SetActive(true);
        }
    }

    void OnTriggerEnter(Collider other) {
        if (other.gameObject.tag == "Pickup1") {
            other.gameObject.SetActive(false);
            count += 1;
        }
        if (other.gameObject.tag == "Pickup2")
        {
            other.gameObject.SetActive(false);
            count += 2;
        }
    }
}
