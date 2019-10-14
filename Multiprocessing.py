from multiprocessing import Process
import numpy as np
import os
import librosa
import time

mfcc_data = []


def readFile(filename):
    branch_soundfile = []
    generator = os.walk(filename, topdown=False)
    for root, dir_file, file_list in generator:
        for data_name in file_list:
            branch_soundfile.append(root + '/' + data_name)
    return branch_soundfile


def ana_data(branch_soundfile):
    global mfcc_data
    for SF in branch_soundfile:
        y, sr = librosa.load(SF, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=24)
        for elem in mfcc:
            mfcc_data.append(elem)
    return


if __name__ == '__main__':
    time_start = time.time()
    filename = 'G:/VoxCeleb2/aac'
    branch_file = readFile(filename)
    branch_file = branch_file[0:1000:1]
    lens = len(branch_file)
    File1 = branch_file[0:lens // 5:1]
    File2 = branch_file[lens // 5:(lens // 5)*2:1]
    File3 = branch_file[(lens // 5)*2:3*(lens // 5):1]
    File4 = branch_file[3 * (lens // 5):4*(lens // 5):1]
    File5 = branch_file[4*(lens // 5):lens:1]
    added_process1 = Process(target=ana_data, args=(File1,))
    added_process2 = Process(target=ana_data, args=(File2,))
    added_process3 = Process(target=ana_data, args=(File3,))
    added_process4 = Process(target=ana_data, args=(File4,))
    added_process5 = Process(target=ana_data, args=(File5,))
    added_process1.start()  # all threads start to process functions
    added_process2.start()
    added_process3.start()
    added_process4.start()
    added_process5.start()

    added_process1.join()  # Until  all threads finish the tasks then Quit at the same time
    added_process2.join()
    added_process3.join()
    added_process4.join()
    added_process5.join()

    np.save("mfcc_data1.npy", mfcc_data)
    time_end = time.time()

    print('total cost:', time_end - time_start)
