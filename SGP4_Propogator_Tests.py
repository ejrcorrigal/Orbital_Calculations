from SGP4_Propogator import *

class SGP4_Propogator_Tests:
    def test_propogator(self, TLE_S, TLE_T, start_julian_date, end_julian_date, julian_date_step):
        Propogator = SGP4_Propogator(TLE_S, TLE_T, start_julian_date, end_julian_date, julian_date_step)
        jd, x, y, z, dx, dy, dz = Propogator.propogate()
        return jd, x, y, z, dx, dy, dz

        
if __name__ == "__main__":

    TLE_S = '1 37846U 11060A   23083.05314641 -.00000107  00000+0  00000+0 0  9993'
    TLE_T = '2 37846  57.0791  13.7465 0004137   4.9723 355.0256  1.70475952 70985'
    start_julian_date = 23083
    end_julian_date = 23085
    julian_date_step = 0.01
    Propogator_Tests = SGP4_Propogator_Tests()
    jd, x, y, z, dx, dy, dz = Propogator_Tests.test_propogator(TLE_S, TLE_T, start_julian_date, end_julian_date, julian_date_step)

    plt.plot(jd, x)
    plt.show()