#import libraries
import numpy as np
import scipy
from scipy import constants
# from numba import jit, prange

#==============================================================================================================================================================================#

#define time step and duration
duration_in_years = 50 #must equate number of years passed to main function
duration_in_seconds = duration_in_years * 31536000 #convert user input to seconds
time_step = 86400 #in seconds, equivalent to 1 day
time = np.arange(0, duration_in_seconds, time_step)
ntime = len(time)

#==============================================================================================================================================================================#

#FUNCTIONS

#function to create between-body position vector array
# @jit(nopython=True, parallel=True)
def create_3d_between_body_position_vector_array(list_of_bodies):
    """
    Takes a list of Body-type objects (with initialised 3d position vector array attributes (of length ntime)) and returns a 'between_body_position_vector_array' of shape 
    (9,9,3,ntime) containing all possible between-body position vectors at all ntime timesteps. 
    e.g. between_body_position_vector_array[0,3,:,:] = all position vectors from the sun to earth, at all time steps in 3 dimensions.
    """
    between_body_position_vector_array = np.empty((9,9,3,ntime))
    for body1_index in np.array((range(9))):
        for body2_index in np.array((range(9))):
            between_body_position_vector_array[body1_index,body2_index,:,:] = list_of_bodies[body2_index].pos_3d_array - list_of_bodies[body1_index].pos_3d_array
    return between_body_position_vector_array


#function to create between-body unit position vector array
# @jit(nopython=True, parallel=True)
def create_3d_between_body_unit_vector_array(between_body_position_vector_array):
    """
    Takes a (9,9,3,ntime)-shape array of between body position vectors and returns a (9,9,3,ntime)-shape array of the unit vectors for each of these. 
    e.g. between_body_unit_vector_array[1,4,:,:] = all unit position vectors from mercury to mars, at all time steps in 3 dimensions.
    """
    between_body_unit_vector_array = np.empty((9,9,3,ntime))
    for body1_index in np.array((range(9))):
        for body2_index in np.array((range(9))):
            if body1_index == body2_index:
                pass
            else:
                between_body_unit_vector_array[body1_index,body2_index,:,:] = between_body_position_vector_array[body1_index, body2_index, :, :]/ np.linalg.norm(between_body_position_vector_array[body1_index, body2_index, :, :])  
    return between_body_unit_vector_array


#function to create between-body force vector array
# @jit(nopython=True, parallel=True)
def create_3d_between_body_force_vector_array(list_of_bodies, between_body_position_vector_array, between_body_unit_vector_array):
    """ 
    Takes a list of Body-type objects, a (9,9,3,ntime)-shape between_body_position_vector_array, and (9,9,3,ntime)-shape between_body_unit_vector_array and returns a 
    (9,9,3,ntime)-shape 
    array of between body force vectors.
    e.g. between_body_force_vector_array[2,5,:,:] = all force vectors from venus to jupiter, at all time steps in 3 dimensions.
    """
    between_body_force_vector_array = np.empty((9,9,3,ntime))
    for body1_index in np.array((range(9))):
        for body2_index in np.array((range(9))):
            if body1_index == body2_index:
                pass
            else:
                between_body_force_vector_array[body1_index,body2_index,:,:] = scipy.constants.G * ((list_of_bodies[body1_index].mass * list_of_bodies[body2_index].mass)/((np.linalg.norm(between_body_position_vector_array[body1_index,body2_index,:,:]))**2)) * between_body_unit_vector_array[body1_index,body2_index,:,:]  
    return between_body_force_vector_array


#function to create total-force-acting-on each body vector array
# @jit(nopython=True, parallel=True)
def create_3d_total_Force_acting_on_array(between_body_force_vector_array):
    """ 
    Takes a between_body_force_vector_array of shape (9,9,3,ntime) and returns a (9,3,ntime)-shape array of the total forces acting on each body.
    e.g. total_Force_acting_on_array[8,:,:] = the total force acting on neptune, at all time steps in 3 dimensions.
    """
    total_Force_acting_on_array = np.empty((9,3,ntime))
    for nth_time in np.array((range(ntime))):      
        for body_index in np.array((range(9))):
            total_Force_acting_on_array[body_index, :, nth_time]= sum(between_body_force_vector_array[body_index,:,:,nth_time])
    return total_Force_acting_on_array


#function to create acceleration for each body vector array
# @jit(nopython=True, parallel=True)
def  create_3d_accelerations_vector_array(list_of_bodies, total_Force_acting_on_array):
    """
    Takes a list of Body-type objects and a (9,3,ntime)-shape array of the total forces acting on each body, and returns a (9,3,ntime)-shape array of the accelarations for 
    each body.
    e.g. acceleration_vector_array[7,:,:] = uranus' acceleration, at all time steps in 3 dimensions.
    """
    acceleration_vector_array = np.empty((9,3,ntime))
    for body_index in np.array((range(9))):
        acceleration_vector_array[body_index, :, :] = total_Force_acting_on_array[body_index, :, :]/list_of_bodies[body_index].mass
    return acceleration_vector_array

