using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class merc_orbit : MonoBehaviour
{
    // Declare string for input file (no extension)
    public string inputfile;
    // Declare list for holding data from CSV reader
    private List<Dictionary<string, object>> MercPositionsList;

    // Indices for columns to be assigned
    private int MerccolumnXindex = 0;
    private int MerccolumnYindex = 1;
    private int MerccolumnZindex = 2;

    // Full column names
    private string MercxName;
    private string MercyName;
    private string MerczName;
    // The object for the data points to be instantiated
    public GameObject Merc;

    // Declare time step variable 
    public int mercury_data_row;
    
    // Set up timer 
    public float timer = 0.0f;
    // Declare vector of coordinates for object to move towards
    public Vector3 merctarget;


    // Declare on_slider_change variable (script for accessing moveduration)
    private on_slider_change on_slider_change;



    // Start is called before the first frame update
    void Start()
    {
        // Set MercPositionsList to results of function Reader with argument inputfile
        MercPositionsList = CSVReader.Read(inputfile);
        // Ensure input file as been read with console log
        Debug.Log(MercPositionsList);

        // Declare list of strings and fill with keys (column names)
        List<string> list_of_MercPositions_columns = new List<string>(MercPositionsList[1].Keys);

        // Assign column name from list of column names to Name variables
        MercxName = list_of_MercPositions_columns[MerccolumnXindex];
        MercyName = list_of_MercPositions_columns[MerccolumnYindex];
        MerczName = list_of_MercPositions_columns[MerccolumnZindex];

        // Initialise Body Position with values at 0th row in MercPositionsList
        float merc_x_initial = System.Convert.ToSingle(MercPositionsList[0][MercxName]);
        float merc_y_initial = System.Convert.ToSingle(MercPositionsList[0][MercyName]);
        float merc_z_initial = System.Convert.ToSingle(MercPositionsList[0][MerczName]);
        Merc.transform.position = new Vector3(merc_x_initial, merc_y_initial, merc_z_initial);

        // Assign on_slider_change script component to on_slider_change variable 
        on_slider_change = GetComponent<on_slider_change>();

        // Initialise mercury data row index variable
        mercury_data_row = 1;
    }

    // Update is called once per frame
    void Update()
    {
        // Increase timer by time elapsed since last update/frame
        timer += Time.deltaTime;

        //Create target Position with values at row index 'mercury_data_row'
        float merc_x = System.Convert.ToSingle(MercPositionsList[mercury_data_row][MercxName]);
        float merc_y = System.Convert.ToSingle(MercPositionsList[mercury_data_row][MercyName]);
        float merc_z = System.Convert.ToSingle(MercPositionsList[mercury_data_row][MerczName]);
        Vector3 merc_target = new Vector3(merc_x, merc_y, merc_z);
        
        // Move Object to position fractionally between current position and target
        Merc.transform.position = Vector3.Lerp(Merc.transform.position, merc_target, timer/on_slider_change.moveduration);

        // Once timer meets/exceeds move duration
        if (timer >= on_slider_change.moveduration)
        {
            // Snap object to target position 
            Merc.transform.position = merc_target;

            // Increase position row index (timestep) by 1, or assign to 0 if at end of simulation 
            if (mercury_data_row < 18250)
            {
                mercury_data_row++;
            }
            else
            {
                mercury_data_row=0;
            }
            // Reset timer for next object move
            timer = 0;
        }
    }
}


