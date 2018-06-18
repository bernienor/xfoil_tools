'''
A collection of xfoil tools for use in python.
Not realy a class, more a collection of usefull functions. The class structure
is used to keep track of filenames, folders and so on for all the helper 
functions in the class.

'''
from subprocess import run


class xfoiltools:
    def __init__(self, load_dir='.\\', save_dir='.\\'):
        self.load_dir = load_dir
        self.save_dir = save_dir
        self.xfoil_input = './xfoil.inp'

    def Repanel_smooth(self, airfoilname, noofpanels, dz=0, dz_pos=0):
        load_name = self.load_dir + airfoilname + '.dat'
        save_name = self.save_dir + airfoilname + '_refined.dat'
        with open(self.xfoil_input, 'w') as f:
            f.write('PLOP\ng\n\n')
            f.write('load \n' + load_name + '\n\n')
            f.write('gdes')
            if(dz > 0):
                f.write('tgap\n' + str(dz) + '\n' + str(dz_pos) + '\n')
                f.write('exec\n')
                f.write('dero')
                f.write('UNIT\n\n\n')
            f.write('MDES\n')
            f.write('FILT\n')
            f.write('FILT\n')
            f.write('FILT\n')
            f.write('FILT\n')
            f.write('FILT\n')
            f.write('EXEC\n\n')

            f.write('ppar\n')
            f.write('N\n')
            f.write(str(noofpanels) + '\n\n\n')
            f.write('save\n' + save_name + '\n\n')
            f.write('quit\n')
        run('c:\\bernt\\bin\\xfoil\\xfoil.exe <' + self.xfoil_input)
