using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    public GameObject prefab;

    // Start is called before the first frame update
    void Start()
    {

        int maxHeight = 9;
        int count = 0;
        for (int height = 0; height <= maxHeight; height++)
        {
            int length = maxHeight - height;
            for (int x = -length; x <= length; x++)
            {
                GameObject obj = null;
                GameObject prev = null;
                for (int z = -length; z <= length; z++)
                {
                    obj = Instantiate(prefab, new Vector3(x * 5.0F, height * 5 + 5, z * 5.0F), Quaternion.identity);
                    obj.name = "Cube" + count;
                    if (obj != null && prev != null)
                    {
                        obj.name = "Cube_joint" + count;
                        SpringJoint fj = obj.AddComponent<SpringJoint>() as SpringJoint;
                        fj.connectedBody = prev.GetComponent<Rigidbody>();
                    }
                    prev = obj;
                    count++;
                }
                
            }
        }

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
