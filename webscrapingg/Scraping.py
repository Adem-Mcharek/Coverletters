#----------------------------------Imports--------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
import os
import numpy as np
import pandas as pd
import openpyxl
import re

#-----------------------------------function----------------------------------------------------------------
def prettyprint(input_string):
    output_string = ''.join([' ' + char if (char.isupper() or char in '$') and prev_char!= ' ' else char for prev_char, char in zip('_' + input_string, input_string)])
    output_string = output_string.lstrip()  # Remove leading space if any
    #print(output_string)
    return(output_string)

def clean_role(input_string):
    # Remove special characters and spaces by replacing them with a single underscore
    cleaned_string = re.sub(r'[^a-zA-Z0-9]+', '_', input_string)
    cleaned_string= cleaned_string.replace(' ', '')
    return cleaned_string

def Scraper(company,role,link,posted,index):

    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text,'lxml')

    elements = soup.find_all('div', class_='text-left')
    L=[element for element in elements]
    L= L[1:]

    with open(f'files/{index}.{company}.{role}.txt', 'w', encoding="utf-8") as f:
        f.write(f'{company}: {role}  ------- {posted}\n \n')

        for element in L:
            element= element.text

            f.write(prettyprint(element))
            f.write('\n')
            f.write('---------------------- \n')
        file= f'files/{index}.{company}.{clean_role(role)}.txt'
        file = file.replace(' ', '')

    return file