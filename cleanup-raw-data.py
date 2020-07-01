# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import re
import os
import pandas as pd 
import numpy as np

pd.options.mode.use_inf_as_na = True

with open('data.csv', 'w') as jobs_info:
    writer = csv.writer(jobs_info)
    
    
    os.remove('data.csv')
    f = open('data.csv', 'a+')

    with open('/Users/vanareddy/Job-Data/file1.csv') as jobs:                                                                                          

        job_reader = pd.read_csv(jobs, delimiter=';', na_values = 'NA').iloc[:, 3:]
        
        for row in range(len(job_reader)):
            #print(str(job_reader.loc[row][0]).split(' '))
            cols = str(job_reader.loc[row][0]).split(' ')
            print(cols)
            if len(cols) <= 17 :
                print(len(cols))
                pass
            else:
                print("Long " + str(len(cols)))
                f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
                                                cols[2], cols[0], cols[1], cols[3], \
                                                cols[23], cols[12], cols[19], cols[5], \
                                                cols[6], cols[4], cols[7], cols[18], cols[14], \
                                                cols[24], cols[9]))
                
            
                f.write("\n")
            f.flush()
            '''
            f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
                                                cols[2], cols[0], cols[1], cols[3], \
                                                cols[23], cols[12], cols[19], cols[5], \
                                                cols[6], cols[4], cols[7], cols[18], cols[14], \
                                              cols[24], cols[9]))
            '''
            
        '''
        for job in job_reader:
            job_col3 = job[3].replace('Resource_List.', '')#.split(' ')
            #row = str(job[0]) + " " + job[1] + " " + job[2] + ' '.join(job_col3)
            row = str(job[0]) + " " + job[1] + " " + job[2] + ' ' + str(job_col3).strip('[]')
            #print(row)
            if not job_col3:
                print("Empty Line")
                f.write("\n")
                pass
            else:
                #print(job_col3)
                #jobnameMD5	userMD5	groupMD5	queue	resources_used_vmem	Resource_List_nodes	
                #Exit_status	qtime	etime	ctime	start	end	Resource_List_walltime	
                #resources_used_walltime	exec_host
                #print(str(job_col3.split(' ')))
                #cols = str(job[3])[0:-1]
                cols = ' '.join(map(str, job_col3.split(' ')))
                print(cols)
                #f.write("{}, ".format(*cols[2]))
                f.write("\n")
                #f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
                #                                cols[2], cols[0], cols[1], cols[3], \
                #                                cols[23], cols[12], cols[19], cols[5], \
                #                                cols[6], cols[4], cols[7], cols[18], cols[14], \
                #                               cols[24], cols[9]))
                
            print("----")
         '''      
