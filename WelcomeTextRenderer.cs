using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;  
using TMPro;       
public class WelcomeTextRenderer : MonoBehaviour
{
    // Declare Welcome Test
    public TextMeshProUGUI WelcomeText; 
    // Time in seconds to display the text
    public float displayTime = 10.0f;  
    // Declare timer 
    private float timer = 0.0f;

    void Start()
    {
        // Ensure the text is visible at the start
        WelcomeText.enabled = true;
    }

    void Update()
    {
        // Increase timer by time elapsed since last update/frame
        timer += Time.deltaTime;

        // If the timer exceeds displayTime, hide the text
        if (timer > displayTime)
        {
            WelcomeText.enabled = false;
        }
    }
}

