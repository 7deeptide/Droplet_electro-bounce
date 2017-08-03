import os, fnmatch, csv
import numpy as np

class Experiment(object):
    def __init__(self, data, name, start=0, end=-1, volume=1, frame_rate=29.95, \
                 outlier=False, threeD=False, charge=1E-11, u0=1):
        self.data = data
        self.name = name
        self.start = start
        self.end = end
        self.volume = volume
        self.frame_rate = frame_rate
        self.outlier = outlier
        self.threeD = threeD
        self.charge = charge
        self.u0 = u0


def import_data(exp_class):
    """
    Takes an experiment type and returns an array of Experiment class objects, with attributes specified by
    a metadata csv. The 'data' attribute The column heads include:
    'R','Area','XM','YM','Major','Minor','Angle','Circ','Slice','AR','Round','Solidity'
    """
    meta_file_location = '../data/' + exp_class + '/meta2.csv'
    datatype = ('U9', int, int, float, float, float, bool, bool)
    metadata = np.genfromtxt(meta_file_location, delimiter=',', dtype=datatype, names=True)
    globals()[exp_class + '_data_list'] = np.array([])
    for drop in metadata:
        if drop['double']==True:
            name = 'drop' + str(drop['name'])
            path = '../data/' + exp_class + '/' + str(drop['name'][:-2:]) + '.csv'
            print(path)
            if name[-1::]=='1':
                data = np.genfromtxt(path, dtype=float, delimiter=',', names=True)
                data = data[0::2]
            else:
                data = np.genfromtxt(path, dtype=float, delimiter=',', names=True)
                data = data[1::2]
        else:
            name = 'drop' + str(drop['name'])
            path = '../data/' + exp_class + '/' + str(drop['name']) + '.csv'
            data = np.genfromtxt(path, dtype=float, delimiter=',', names=True)      
        start = drop['start']
        end = drop['end']
        volume = drop['volume']
        surfaceV = drop['surfaceV']
        frame_rate = drop['frame_rate']
        outlier = drop['outlier']
        double = drop['double']
        globals()[str(name)] = Experiment(data, name, start, end, volume, surfaceV, \
                                                           frame_rate, outlier, double)
        globals()[exp_class + '_data_list'] = np.append(globals()[exp_class + '_data_list'], \
                                                        globals()[str(name)])