# import libraries
import numpy as np
import scipy
from scipy import constants

#==============================================================================================================================================================================#

#define time step and duration
duration_in_years = 50 #must equate number of years passed to main function

duration_in_seconds = duration_in_years * 31536000 #convert user input to seconds
time_step = 86400 #in seconds, equivalent to 1 day
time = np.arange(0, duration_in_seconds, time_step)
ntime = len(time)

#==============================================================================================================================================================================#

# FUNCTIONS

# function to find new positions
def find_new_3d_positions(i,list_of_bodies,acceleration_vector_array):
    """
    Finds the position of each body at the following time step i+1, where i is the current timestep
    """
    for body_index in np.array((range(9))):
        list_of_bodies[body_index].pos_3d_array.T[i+1] = list_of_bodies[body_index].pos_3d_array.T[i] + (list_of_bodies[body_index].vel_3d_array[:, i]*time_step) + ((1/2) * acceleration_vector_array[body_index,:,i].T * (time_step)**2) #all things added should be shape 1x3
    return None

# function to update between_body_position_vector_array
def find_new_between_body_position_vectors(i,list_of_bodies,between_body_position_vector_array):
    """
    Finds the between-body position vectors at the following time step i+1, where i is the current timestep
    """
    for body1_index in np.array((range(9))):
        for body2_index in np.array((range(9))):
            between_body_position_vector_array[body1_index,body2_index,:,i+1] = list_of_bodies[body2_index].pos_3d_array[:,i+1] - list_of_bodies[body1_index].pos_3d_array[:,i+1]
    return None
    
# function to update between_body_unit_vector_array
def find_new_between_body_unit_vectors(i,between_body_unit_vector_array,between_body_position_vector_array):
    """
    Finds the between-body unit vectors at the following time step i+1, where i is the current timestep
    """
    for body1_index in np.array((range(9))):
        for body2_index in np.array((range(9))):
            if body1_index == body2_index:
                pass
            else:
                between_body_unit_vector_array[body1_index,body2_index,:,i+1] =  between_body_position_vector_array[body1_index,body2_index,:,i+1] / np.linalg.norm(between_body_position_vector_array[body1_index,body2_index,:,i+1])
    return None
    
# function to update between_body_force_vector_array
def find_new_between_body_force_vectors(i,list_of_bodies,between_body_position_vector_array,between_body_unit_vector_array,between_body_force_vector_array):
    """
    Finds the between-body force vectors at the following time step i+1, where i is the current timestep
    """
    for body1_index in np.array((range(9))):
        for body2_index in np.array((range(9))): 
            if body1_index == body2_index:
                pass
            else:
                between_body_force_vector_array[body1_index,body2_index,:,i+1] =  scipy.constants.G * ((list_of_bodies[body1_index].mass * list_of_bodies[body2_index].mass) / ((np.linalg.norm(between_body_position_vector_array[body1_index,body2_index,:,i+1]))**2)) * between_body_unit_vector_array[body1_index,body2_index,:,i+1]
    return None

# function to update total_Force_acting_on_array
def find_new_total_Force_acting_on_vectors(i,between_body_force_vector_array,total_Force_acting_on_array):
    """
    Finds the total Force acting on vectors at the following time step i+1, where i is the current timestep
    """
    for body_index in np.array((range(9))):
        total_Force_acting_on_array[body_index, :, i+1]= sum(between_body_force_vector_array[body_index,:,:,i+1])
    return None 

# function to update acceleration_vector_array
def find_new_acceleration_vectors(i,list_of_bodies,acceleration_vector_array,total_Force_acting_on_array):
    """
    Finds the acceleration vectors at the following time step i+1, where i is the current timestep
    """
    for body_index in np.array((range(9))):
        acceleration_vector_array[body_index, :, i+1] = total_Force_acting_on_array[body_index, :, i+1]/list_of_bodies[body_index].mass
    return None
    
# function to update body.vel_3d_array
def find_new_velocity_vectors(i,list_of_bodies,acceleration_vector_array):
    """
    Finds the velocity vectors at the following time step i+1, where i is the current timestep
    """
    for body_index in np.array((range(9))):
        list_of_bodies[body_index].vel_3d_array[:, i] = list_of_bodies[body_index].vel_3d_array[:, i-1] + (time_step/2 * acceleration_vector_array[body_index, :, i]) + (time_step/2 * acceleration_vector_array[body_index, :, i-1])
    return None