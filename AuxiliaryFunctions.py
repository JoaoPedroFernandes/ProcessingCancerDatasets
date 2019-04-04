# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:16:38 2018

@author: JF
"""

import colorama as c #color text (ver melhor depois como aplicar)
from colorama import Fore #color text (ver melhor depois como aplicar)

import os

import Menu as M
import TextReturningFunctions as TRF



### Auxiliary I/O Functions ###
def back_or_quit():
    print('\nDo you want to go back to the main menu (b) or quit the program (q)?')
    while True:                
        suboption = str(input('Select your intention: '))
        if suboption.lower() == 'b':
            return M.MainMenu()
        elif suboption.lower() == 'q':
            return TRF.quit_func()
        else:
            print("Invalid choice. Please select 'b' to go back to the main menu or 'q' to exit the program.")
    exit

def waiting_message():
    import sys
    print("\n\nPlease wait. This may take some time.\n")
    print ("\nThe file is being processed.\nWe'll let you know when the process is over.\n")
    print("\nTo quit the program while its runnig, press:\n\t - on cmd terminal: CTRL + C\n\t - on python interface console: CTRL + Q\n")
    sys.stdout.flush()

def create_input_dir():
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Input_Files' 
    if not os.path.exists(cwd):
        os.mkdir(cwd)
        print('\nA new directory to store the input files was created.')
    else:
        print('\nThere is already a current directory for the input files storage.')
    
def create_output_dir():
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Output_Files' 
    if not os.path.exists(cwd):
        os.mkdir(cwd)
        print('\nA new directory to store the output files was created.')
    else:
        print('\nThere is already a current directory for the output files storage.')

def write_in_out_dir():
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Output_Files\\'
    if not os.path.exists(cwd):
        os.mkdir(cwd)
        return cwd
    else:
        return cwd


def read_input_files():
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Input_Files\\'
    if not os.path.exists(cwd):
        os.mkdir(cwd)
        return cwd
    else:
        return cwd


def create_met_dir():
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Input_Files' + '\\' + 'Methylation_Tables'
    if not os.path.exists(cwd):
        os.mkdir(cwd)
        print('\nA new directory to store the methylation files was created within the Input Files directory.')
    else:
        print('\nThere is already a current directory for the methylation files storage within the Input Files directory.')
    
def read_met_files():
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Input_Files\\' + '\\' + 'Methylation_Tables'
    if not os.path.exists(cwd):
        os.mkdir(cwd)
        return cwd
    else:
        return cwd



### Main ###
if __name__ == "__main__":
    pass