using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    [SerializeField] ParticleSystem snow;
    [SerializeField] ParticleSystem rain;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("p"))
        {
            if (snow.isEmitting) snow.Stop();
            else snow.Play();
        }
        if (Input.GetKeyDown("o"))
        {
            if (rain.isEmitting) rain.Stop();
            else rain.Play();
        }
    }
}
