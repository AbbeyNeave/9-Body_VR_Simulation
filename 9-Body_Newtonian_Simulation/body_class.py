# import libraries
import numpy as np

#==============================================================================================================================================================================#

# define constants (time step and duration)
duration_in_years = 50 #must equate number of years passed to main function
duration_in_days = duration_in_years * 365.24 #conver user input to days
time_step = 1   #in days
time = np.arange(0, duration_in_days, time_step)
ntime = len(time)

#==============================================================================================================================================================================#

# create planet class
class Body:
    def __init__(self, mass, initial_pos, initial_vel):
        self.mass = mass
        self.initial_pos = initial_pos
        self.initial_vel = initial_vel
        self.xpos_1d_series = np.empty(ntime)
        self.ypos_1d_series = np.empty(ntime)
        self.zpos_1d_series = np.empty(ntime)
        self.xpos_1d_series[0] = initial_pos[0]
        self.ypos_1d_series[0] = initial_pos[1]
        self.zpos_1d_series[0] = initial_pos[2]
        self.pos_3d_array = np.array([self.xpos_1d_series, self.ypos_1d_series, self.zpos_1d_series]) #of shape (18262,3)
        self.vel_3d_array = np.empty((3, ntime))
        self.vel_3d_array[:, 0] = self.initial_vel
    def __str__(self):
        return f"Mass: {self.mass}, Initialised 3D Position Vector Array: {self.pos_3d_array}, Initialised 3D Velocity Vector Array: {self.vel_3d_array}"
    def __repr__(self):
        return f"Mass: {self.mass}, Initialised 3D Position Vector Array: {self.pos_3d_array}, Initialised 3D Velocity Vector Array: {self.vel_3d_array}"
