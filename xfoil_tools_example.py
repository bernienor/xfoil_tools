'''
ag455ct02r.dat origins from http://airfoiltools.com/airfoil/details?airfoil=ag455ct02r-il

'''

import xfoil_tools as xfoil
xf = xfoil.xfoiltools(load_dir='.\\', save_dir='.\\')
xf.Repanel_smooth('ag455ct02r', 800)
#xf.swexport(airfoilname='ag455ct02r_refined.dat')
xf.swexport(airfoilname='ag455ct02r_refined.dat', filename='ag455_sw.txt')
