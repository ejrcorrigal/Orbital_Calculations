import numpy as np
import matplotlib.pyplot as plt
from sgp4.api import Satrec

class SGP4_Propogator:
    def __init__(self, TLE_S, TLE_T, start_julian_date, end_julian_date, julian_date_step):
        self.TLE_S = TLE_S
        self.TLE_T = TLE_T
        self.start_julian_date = start_julian_date
        self.end_julian_date = end_julian_date
        self.julian_date_step = julian_date_step

        self.julian_date_array = np.arange(start_julian_date, end_julian_date, julian_date_step)
        print(len(self.julian_date_array))
        self.satellite = Satrec.twoline2rv(self.TLE_S, self.TLE_T)
        
    def propogate(self):
        julian_fraction = self.julian_date_array%1
        print(self.julian_date_array)
        julian_day_array = self.julian_date_array.astype(int)
        x_positions = np.zeros((len(julian_fraction)))
        y_positions = np.zeros((len(julian_fraction)))
        z_positions = np.zeros((len(julian_fraction)))

        x_velocities = np.zeros((len(julian_fraction)))
        y_velocities = np.zeros((len(julian_fraction)))
        z_velocities = np.zeros((len(julian_fraction)))
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
        print(error)
        return error

    def format_orbital_vectors(self, vector):
        x_components = vector[:, 0]
        y_components = vector[:, 1]
        z_components = vector[:, 2]

        x_components = np.asarray(x_components)
        y_components = np.asarray(y_components)
        z_components = np.asarray(z_components)

        return x_components, y_components, z_components

if __name__ == "__main__":
    TLE_S = '1 23839U 96020A   23083.12882862  .00000079  00000+0  00000+0 0  9999'
    TLE_T = '2 23839   8.1196  56.2378 0004719 335.9421 217.7025  0.99993763 98445'
    start_julian_date = 230805
    end_julian_date = 23087
    julian_date_step = 0.1
    Propogator = SGP4_Propogator(TLE_S, TLE_T, start_julian_date, end_julian_date, julian_date_step)
    jd_array, x, y, z, dx, dy, dz = Propogator.propogate()
    radius = (x**2 + y**2 + x**2)**0.5
    plt.plot(jd_array, radius)
    plt.show()
