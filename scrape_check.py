#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:59:42 2022

@author: alexb
"""

"""Checks that all the scraped data has the correct number of rows
and no duplicate rows."""

import pandas as pd

correct_row_nums = {'2014': 791,
                    '2015': 1124,
                    '2016': 1215,
                    '2017': 1320,
                    '2018': 1129,
                    '2019': 1089,
                    '2020': 1162,
                    '2021': 932,
                    '2022': 804
                    }

for year in range(2014, 2023):
    year_str = str(year)
    df = pd.read_csv(f'{year_str}_fresh15.csv')
    valid = True
    
    #Checks for duplicated rows:
    if not df[df.duplicated()].empty:
        valid = False
        print(f'{year_str} results file has duplicate rows.')
    
    #Checks for the correct number of rows:
    if len(df) != correct_row_nums[year_str]:
        valid = False
        file_rows = len(df)
        correct_rows = correct_row_nums[year_str]
        print(f'{year_str} results file has {file_rows} rows, but should have {correct_rows} rows.')
    
    #Prints a message if neither of the errors above occurs:        
    if valid == True:
        print (f'{year_str}: Good!')
              
    