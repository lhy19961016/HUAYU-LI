import numpy as np
import os
import librosa
import time


def readFile(filename):
    branch_soundfile = []
    generator = os.walk(filename, topdown=False)
    for root, dir_file, file_list in generator:
        for data_name in file_list:
            branch_soundfile.append(root+'/'+data_name)
    return branch_soundfile


def ana_data(branch_soundfile):
    mfcc_data = []
    for sound_file in branch_soundfile:
        y, sr = librosa.load(sound_file, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=24)
        for elem in mfcc:
            mfcc_data.append(elem)
    return mfcc_data


if __name__ == '__main__':
    time_start = time.time()
    filename = 'G:/VoxCeleb2/aac'
    branch_file = readFile(filename)
    branch_file = branch_file[0:1000:1]
    ana_file = ana_data(branch_file)
    np.save("mfcc_data0.npy", ana_file)
    time_end = time.time()
    print('total cost:', time_end - time_start)
