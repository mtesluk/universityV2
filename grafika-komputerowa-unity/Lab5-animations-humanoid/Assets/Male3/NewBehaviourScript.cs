using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    [SerializeField] private Animator my = null;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("space"))
        {
            Debug.Log("Spinning");
            my.Play("movehead");
        }
        if (Input.GetKeyUp("space"))
        {
            Debug.Log("Spinning");
            my.Play("nic");
        }
    }
}
