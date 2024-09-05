using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;  
using UnityEngine.XR.Interaction.Toolkit;
using TMPro;  

public class merc_show_factsheet_script : MonoBehaviour
{ 
    // Declare interactable object
    public XRBaseInteractable mercury;
    // Declare factsheet to be shown 
    public TextMeshProUGUI mercury_factsheet; 
    // Declare maximum time for factsheet to be shown
    private float displayTime = 8f;
    // Declare all other factsheet
    public TextMeshProUGUI sun_factsheet;
    public TextMeshProUGUI venus_factsheet;
    public TextMeshProUGUI earth_factsheet;
    public TextMeshProUGUI mars_factsheet;
    public TextMeshProUGUI jupiter_factsheet;
    public TextMeshProUGUI saturn_factsheet;
    public TextMeshProUGUI uranus_factsheet;
    public TextMeshProUGUI neptune_factsheet;

    // Awake is called before the programme begins
    void Awake()
    {
        // Ensure factsheet is not visible at start
        mercury_factsheet.enabled = false;  
        // Listen for object's 'selectEntered' and call OnSelectEntered method when object is selected
        mercury.selectEntered.AddListener(OnSelectEntered);  
    }

    // Method called when the interactable object is selected
    public void OnSelectEntered(SelectEnterEventArgs args)
    {
        // On select event, start coroutine
        StartCoroutine(ShowFactSheet());
    }

    // Coroutine to show factsheet for a limited time
    private IEnumerator ShowFactSheet()
    {
        // Enable the relevant factsheet
        mercury_factsheet.enabled = true;
        // Disable all other factsheets
        sun_factsheet.enabled = false;
        venus_factsheet.enabled = false;
        earth_factsheet.enabled = false;
        mars_factsheet.enabled = false;
        jupiter_factsheet.enabled = false;
        saturn_factsheet.enabled = false;
        uranus_factsheet.enabled = false;
        neptune_factsheet.enabled = false;
        // Wait for the specified time
        yield return new WaitForSeconds(displayTime);  
        // Disable relevant factsheet after specified time
        mercury_factsheet.enabled = false;
    }
}
