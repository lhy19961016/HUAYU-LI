import numpy as np
import librosa
import time
import threading
import os

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
    lens = len(branch_file)
    File1 = branch_file[0:lens // 4:1]
    File2 = branch_file[lens // 4:lens // 2:1]
    File3 = branch_file[lens // 2:3 * lens // 4:1]
    File4 = branch_file[3 * lens // 4:lens:1]
    added_thread1 = threading.Thread(target=ana_data, name='Thread No.1', args=(File1,))
    added_thread2 = threading.Thread(target=ana_data, name='Thread No.2', args=(File2,))
    added_thread3 = threading.Thread(target=ana_data, name='Thread No.3', args=(File3,))
    added_thread4 = threading.Thread(target=ana_data, name='Thread No.4', args=(File4,))

    added_thread1.start()  # all threads start to process functions
    added_thread2.start()
    added_thread3.start()
    added_thread4.start()

    added_thread1.join()  # Until  all threads finish the tasks then Quit at the same time
    added_thread2.join()
    added_thread3.join()
    added_thread4.join()

    np.save("mfcc_data.npy", mfcc_data)
    print(mfcc_data)
    print(len(mfcc_data))
    time_end = time.time()

    print('total cost:', time_end - time_start)
