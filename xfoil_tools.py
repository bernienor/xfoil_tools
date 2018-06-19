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

    def output(self, data, file=None):
        ''' Helper function to simplify writing to file or to stdout '''
        if(file):
            file.write(data)
            file.write('\n')
        else:
            print(data)

    def Repanel_smooth(self, airfoilname, noofpanels, dz=0, dz_pos=0):
        load_name = self.load_dir + airfoilname + '.dat'
        save_name = self.save_dir + airfoilname + '_refined.dat'
        xfoil_input = list()
        xfoil_input.append('PLOP\ng\n\n')
        xfoil_input.append('load \n' + load_name + '\n\n')
        xfoil_input.append('gdes')
        if(dz > 0):
            xfoil_input.append('tgap\n' + str(dz) + '\n' + str(dz_pos) + '\n')
            xfoil_input.append('exec\n')
            xfoil_input.append('dero')
            xfoil_input.append('UNIT\n\n\n')
        xfoil_input.append('MDES\n')
        xfoil_input.append('FILT\n')
        xfoil_input.append('FILT\n')
        xfoil_input.append('FILT\n')
        xfoil_input.append('FILT\n')
        xfoil_input.append('FILT\n')
        xfoil_input.append('EXEC\n\n')

        xfoil_input.append('ppar\n')
        xfoil_input.append('N\n')
        xfoil_input.append(str(noofpanels) + '\n\n\n')
        xfoil_input.append('save\n' + save_name + '\n\n')
        xfoil_input.append('quit\n')
        commands = bytearray()
        for command in xfoil_input:
            commands = commands + bytearray(command, 'utf8')
        run('c:\\bernt\\bin\\xfoil\\xfoil.exe', input=commands)

    def swexport(self, airfoilname, filename=None, Z=0.0):
        ''' Exports the given airfoil file to a SolidWorks curve line in X, Y
            plane at the given Z height. Writes to file if a filename is given.
        '''
        try:
            outputfile = open(filename, 'w')
        except(FileNotFoundError, TypeError):
            print('\n\nException!!!\n\n')
            outputfile = None
        with open(airfoilname) as airfoilfile:
            next(airfoilfile)  # Skip xfoil header
            for line in airfoilfile:
                data = line.split()
                self.output(str(data[0]) + '\t' + str(data[1]) +
                            '\t' + str(Z), outputfile)
