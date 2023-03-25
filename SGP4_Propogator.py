import numpy as np
import matplotlib.pyplot as plt
from sgp4.api import Satrec
from sgp4.api import SGP4_ERRORS

class SGP4_Propogator:
    def __init__(self, TLE_S, TLE_T, start_julian_date, end_julian_date, julian_date_step):
        self.TLE_S = TLE_S
        self.TLE_T = TLE_T
        self.start_julian_date = start_julian_date
        self.end_julian_date = end_julian_date
        self.julian_date_step = julian_date_step

        self.julian_date_array = np.arange(start_julian_date, end_julian_date, julian_date_step)
        self.satellite = Satrec.twoline2rv(self.TLE_S, self.TLE_T)
        
    def propogate(self):
        julian_fraction = self.julian_date_array%1
        julian_day_array = self.julian_date_array.astype(int)
        
        x_positions = np.zeros((len(julian_fraction)))
        y_positions = np.zeros((len(julian_fraction)))
        z_positions = np.zeros((len(julian_fraction)))

        x_velocities = np.zeros((len(julian_fraction)))
        y_velocities = np.zeros((len(julian_fraction)))
        z_velocities = np.zeros((len(julian_fraction)))

        #TODO Try to vectorize this loop
        for i in range(len(julian_fraction)):
            error, r, v = self.satellite.sgp4(julian_day_array[i], julian_fraction[i])
            self.handle_sgp4_error(error)
            x_positions[i] = r[0]
            y_positions[i] = r[1]
            z_positions[i] = r[2]

            x_velocities[i] = v[0]
            y_velocities[i] = v[1]
            z_velocities[i] = v[2]

        return self.julian_date_array, x_positions, y_positions, z_positions, x_velocities, y_velocities, z_velocities
    def handle_sgp4_error(self, error):
        #TODO
        output = 'No error'
        try:
            error_meaning = SGP4_ERRORS[error]
            output = error_meaning
        except:
            pass
        return output

    def format_orbital_vectors(self, vector):
        x_components = vector[:, 0]
        y_components = vector[:, 1]
        z_components = vector[:, 2]

        x_components = np.asarray(x_components)
        y_components = np.asarray(y_components)
        z_components = np.asarray(z_components)

        return x_components, y_components, z_components