# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd 
from sys import exit

pd.options.mode.use_inf_as_na = True

def cleanupData(raw_data_path, cleaned_data_path):
    
    dir_conts = os.listdir(raw_data_path)
    for file in dir_conts:
        
        csv_filename = os.path.splitext(file)[0]
        
        file = raw_data_path + '/' + file
        
        #remove file if it exists
        csv_filename = cleaned_data_path + '/' + csv_filename + '.csv'
        #os.remove(filename)
        #create new csv file
        f = open(csv_filename, 'w+')
        
        #write header
        f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
                            'jobnameMD5', 'userMD5', 'groupMD5', 'queue', 'resources_used_vmem',\
                          'Resource_List_nodes', 'Exit_status', 'qtime', 'etime', 'ctime',	'start',\
                          'end', 'Resource_List_walltime',	'resources_used_walltime', 'exec_host'))
        f.write("\n")
    
        with open(file) as jobs:                                                                                          
    
            job_reader = pd.read_csv(jobs, delimiter=';', na_values = 'NA').iloc[:, 3:]
            
            for row in range(len(job_reader)):
                cols = str(job_reader.loc[row][0]).split(' ')
                #print(cols)
                if len(cols) <= 17 :
                    #print(len(cols))
                    pass
                elif len(cols) == 25:
                    #write data
                    f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
                                                    cols[2].split('=')[1], cols[0].split('=')[1], \
                                                    cols[1].split('=')[1], cols[3].split('=')[1], \
                                                    cols[23].split('=')[1], cols[12].split('=')[1], \
                                                    cols[19].split('=')[1], cols[5].split('=')[1], \
                                                    cols[6].split('=')[1], cols[4].split('=')[1], \
                                                    cols[7].split('=')[1], cols[18].split('=')[1], \
                                                    cols[14].split('=')[1], cols[24].split('=')[1], \
                                                    cols[9].split('=')[1]))
                    f.write("\n")
                else:
                    #write data
                    f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
                                                    cols[2].split('=')[1], cols[0].split('=')[1], \
                                                    cols[1].split('=')[1], cols[3].split('=')[1], \
                                                    cols[24].split('=')[1], cols[13].split('=')[1], \
                                                    cols[20].split('=')[1], cols[5].split('=')[1], \
                                                    cols[6].split('=')[1], cols[4].split('=')[1], \
                                                    cols[7].split('=')[1], cols[19].split('=')[1], \
                                                    cols[15].split('=')[1], cols[25].split('=')[1], \
                                                    cols[9].split('=')[1]))
                    f.write("\n")   
                f.flush()
            
if __name__ == "__main__":
    raw_data_path = '/Users/vanareddy/Job-Data/IU/Mason-Oct-Dec-AcctFiles'
    cleaned_data_path = '/Users/vanareddy/Job-Data/IU-Data'
    
    cleanupData(raw_data_path, cleaned_data_path)

