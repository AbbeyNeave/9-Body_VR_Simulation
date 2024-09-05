using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class on_slider_change : MonoBehaviour
{
    // Declare slider object to listen to
    public Slider slider;
    // Declare new variable moveduration which the slider's position determines
    public float moveduration;

    // Awake is called before the programme begins
    void Awake()
    {
        // Initialise the sliders value at 2 (1 month/second)
        slider.value = 2;
        // // Initialise the move duration at 1/30 (1 month/second)
        moveduration = 1f/30f;
        // Listen for Slider's 'onValueChanged' event and call OnSliderValueChanged method when slider's value is changed
        slider.onValueChanged.AddListener(OnSliderValueChanged);
    }

    // Method called when the user changes the slider value
    void OnSliderValueChanged(float value)
    {
        if (slider.value == 0) // If slider at value 0
        {
            moveduration = 1f; // Each simulated day increase should last 1 real second
        }
        else if (slider.value == 1)  // If slider at value 1
        {
            moveduration = 1f/7f; // Each simulated day increase should last 1/7 real second
        }
        else if (slider.value == 2) // If slider at value 2
        {
            moveduration = 1f/30f; // Each simulated day increase should last 1/30 real second
        }
        else if (slider.value == 3)  // If slider at value 3
        {
            moveduration = 1f/90f; // Each simulated day increase should last 1/90 real second
        }
    }
}

