import os
from glob import glob as glob
import subprocess
import shutil
import multiprocessing as mp


target_dir = '/compute'

folders = glob(target_dir + '/*')

def delete_folder(folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
        #print(folder)


N= mp.cpu_count()



with mp.Pool(processes = N) as p:
    results = p.map(delete_folder, [f'{folder}/vayzenbe' for folder in folders])

