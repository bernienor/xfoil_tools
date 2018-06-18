'''
ag455ct02r.dat origins from http://airfoiltools.com/airfoil/details?airfoil=ag455ct02r-il

'''


import xfoil_tools as xfoil
xf = xfoil.xfoiltools()
xf.Repanel_smooth('ag455ct02r.dat', 400)
