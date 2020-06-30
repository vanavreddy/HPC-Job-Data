# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import re

with open('data.csv', 'w') as words:
    writer = csv.writer(words)

    with open('/Users/vanareddy/Job-Data/file1.csv') as jobs:                                                                                          
        job_reader = csv.reader(jobs, delimiter=';')
        for job in job_reader:
            job = job[3].replace('Resource_List.', '').replace(':', ' ')
            print(job)
            '''
            for words in job: 
                space_words = re.split('\.', words)
                print(space_words)
                
                for word in split_words:
                    print(word.split(':'))
                    writer.writerow(word.split(':'))
            '''
            print("----")
                
                
                
