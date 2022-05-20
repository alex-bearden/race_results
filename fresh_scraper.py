#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:04:20 2022

@author: alexb
"""

#Scrapes results of Fresh 15k, 2014-2022.

from helium import *
import pandas as pd
import time

urls = {
    '2014': 'https://trinitytiming.com/results/#/race/vtYqn2/15/',
    '2015': 'https://trinitytiming.com/results/#/race/9bew7T/15/',
    '2016': 'https://trinitytiming.com/results/#/race/aoz3hr/15/',
    '2017': 'https://trinitytiming.com/results/#/race/4AC5uK/15/',
    '2018': 'https://trinitytiming.com/results/#/race/ogcwgb/15/',
    '2019': 'https://trinitytiming.com/results/#/race/q3fh9d/15/',
    '2020': 'https://trinitytiming.com/results/#/race/aKoMUO/15/',
    '2021': 'https://trinitytiming.com/results/#/race/3HPkTR/15/',
    '2022': 'https://trinitytiming.com/results/#/race/enNQDQ/15/'
}

#Scrapes the desired information off a page and appends it to results_array:
def scrape_and_append(results_array):
    page_results = find_all(S('.highlited'))
    if len(page_results) != 0:
        for row in page_results:
            row_list = [entry.text for entry in row.web_element.find_elements_by_tag_name('td')[1:]]
            results_array.append(row_list)
    return results_array

#Converts an array with scraped info into a labeled pandas df:
def array_to_df(results_array):
    attributes = ['Place', 'Div', 'Div_place', 'Name', 'Age', 'City', 'State', 'Bib', 
              '5k_split', '10k_split', 'Last_5k_split', 'Time']
    results_df = pd.DataFrame(results_array, columns=attributes)
    return results_df

#Same as above, but for the 2014 data (which has less columns):
def array_to_df_2014(results_array):
    attributes = ['Place', 'Div', 'Div_place', 'Name', 'Age', 'City', 'State', 'Bib', 
              '10k_split', 'Time']
    results_df = pd.DataFrame(results_array, columns=attributes)
    return results_df

#Scrapes each page from one year of the Fresh 15:
def fresh_15_scrape(year):
    start_chrome(urls[year], headless=False)
    wait_until(Text('Place').exists)
    results_array = scrape_and_append([])
    
    #Clicks and scrapes until there's nothing left to get:
    while Text('>>').exists():
        click('>>')
        time.sleep(5)
        if Text('No Results Yet').exists():
            break
        else:
            results_array = scrape_and_append(results_array)
    
    kill_browser()
    
    #Converts the array with scraped info into a pandas df:
    if year == '2014':
        results_df = array_to_df_2014(results_array)
        results_df.to_csv(f'{year}_fresh15.csv', index=False)
    else:
        results_df = array_to_df(results_array)
        results_df.to_csv(f'{year}_fresh15.csv', index=False)
    
    print(f'{year}: Done')
    
for year in urls.keys():
    fresh_15_scrape(year)