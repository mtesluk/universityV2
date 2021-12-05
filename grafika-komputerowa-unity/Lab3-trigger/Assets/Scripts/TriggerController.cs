using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class TriggerController : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.GetComponent<Collider>().CompareTag("Player"))
        {
            AudioSource sound = other.GetComponent<AudioSource>();
            sound.Play();
        }
    }
}
