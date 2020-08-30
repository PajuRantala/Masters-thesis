# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:29:59 2020

@author: Koti
"""

import os
from os import path

csv_dir = r'F:\dippa\processed\coreg_logs'

def main():
    files = [f for f in os.listdir(csv_dir) if path.isfile(csv_dir + '\\'+f)]
    print(files)
    no_hs = open(csv_dir + r'\no_hs_distances.csv', 'w')
    hs = open(csv_dir + r'\hs_distances.csv', 'w')
    for f in files:
        if f[-7:-3] == '_hs.':
            r = open(csv_dir + '\\' + f)
            l = map(lambda y:list(filter(lambda x: x != '', y)), map(lambda x: x.rstrip().replace('[','').replace(']','').split(' '), r.readlines()[4:]))
            for err in [item for sublist in l for item in sublist]:
                no_hs.write(err+'\n')
        elif f[-4:] == '.csv':
            r = open(csv_dir + '\\' + f)
            l = map(lambda y:list(filter(lambda x: x != '', y)), map(lambda x: x.rstrip().replace('[','').replace(']','').split(' '), r.readlines()[4:]))
            for err in [item for sublist in l for item in sublist]:
                hs.write(err+'\n')
    no_hs.close()
    hs.close()
    
    
if __name__ == '__main__':
    main()