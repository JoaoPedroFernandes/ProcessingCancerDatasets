# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:49:57 2018

@author: JF
"""


import MenusMainFunctions as MMF
import TextReturningFunctions as TRF
import AuxiliaryFunctions as AF

import warnings
warnings.filterwarnings("ignore")


### Main Menu Program ###  
def MainMenu():
    ans = True
    while ans:
        TRF.main_menu_text()
        return MMF.main_menu_func()
    exit

def submenu():
    ans = True
    while ans:
        TRF.submenu_text()
        return MMF.submenu_func()
    exit

def process_data_menu():
    ans = True
    while ans:
        TRF.process_data_menu_text()
        return MMF.process_data_menu_func()
    exit

def get_files_menu():
    ans = True
    while ans:
        TRF.get_files_menu_text()
        option = input('Select an option: ')
        if option.lower() == 'b':
            return submenu()
        elif option.lower() == "q":
            return TRF.quit_func()
        elif option.lower() == '1':
            return MMF.get_files_menu_opt1_func()
        elif option.lower() == '2':
            return MMF.get_files_menu_opt2_func()
        elif option.lower() == '3':
            return MMF.get_files_menu_opt3_func()
        else:
            print(TRF.invalid_select())
            return get_files_menu()
    exit

def load_files_menu():
    ans = True
    while ans:
        TRF.load_files_menu_text()
        option = input('Select an option: ')
        if option.lower() == 'b':
            return submenu()
        elif option.lower() == "q":
            return TRF.quit_func()
        elif option.lower() == '1':
            return MMF.load_input_files_menu_func()
        elif option.lower() == '2':
            return MMF.load_input_files_menu_func()
        elif option.lower() == '3':
            return MMF.load_input_files_menu_func()
        elif option.lower() == '4':
            return MMF.load_input_files_menu_func()
        elif option.lower() == '5':
            return MMF.load_input_files_menu_opt5_func()
        else:
            print(TRF.invalid_select())
            return load_files_menu()
    exit

def associated_probs_calcul_menu():
    ans = True
    while ans:
        TRF.associated_probs_calcul_menu_text()
        return MMF.associated_probs_calcul_menu_func()
    exit

def metadata_associated_prob_menu():
    ans = True
    while ans:
        TRF.associated_probs_metadata_menu_text()
        option = input('Select an option: ')
        if option.lower() == 'b':
            return associated_probs_calcul_menu()
        elif option.lower() == "q":
            return TRF.quit_func()
        elif option == '1':
            return MMF.prob_metadata_menu_opt1_func()
        else:
            print(TRF.invalid_select())
            return metadata_associated_prob_menu()
    exit

def mut_associated_prob_menu():
    ans = True
    while ans:
        TRF.associated_probs_mutations_menu_text()
        option = input('Select an option: ')
        if option.lower() == 'b':
            return associated_probs_calcul_menu()
        elif option.lower() == "q":
            return TRF.quit_func()
        elif option.lower() == '1':
            return MMF.prob_mutations_menu_opt1_func()
        elif option.lower() == '2':
            return MMF.prob_mutations_menu_opt2_func()
        elif option.lower() == '3':
            return MMF.prob_mutations_menu_opt3_func()
        elif option.lower() == '4':
            return MMF.prob_mutations_menu_opt4_func()
        else:
            print(TRF.invalid_select())
            return mut_associated_prob_menu()
    exit


def met_associated_prob_menu():
    ans = True
    while ans:
        TRF.associated_probs_methylation_menu_text()
        option = input('Select an option: ')
        
        if option.lower() == 'b':
            return associated_probs_calcul_menu()
        
        elif option.lower() == 'q':
            return TRF.quit_func()
        
        elif option.lower() == '1':
            return MMF.prob_methylation_menu_opt1_func()
            
        else:
            print(TRF.invalid_select())
            return met_associated_prob_menu()
    exit

def genetic_expression_associated_prob_menu():
    ans = True
    while ans:
        TRF.associated_probs_ge_menu_text()
        option = input('Select an option: ')
        
        if option.lower() == 'b':
            return associated_probs_calcul_menu()

        elif option.lower() == 'q':
            return TRF.quit_func()
        
        elif option.lower() == '1':
            return MMF.prob_genexp_menu_opt1_func()
        
        else:
            print(TRF.invalid_select())
            return genetic_expression_associated_prob_menu()
    exit            
   


def simple_process_data_menu():
    ans = True
    while ans:
        TRF.simple_process_data_menu_text()
        option = input('Select an option: ')
        if option.lower() == 'b':
            return process_data_menu()
        elif option.lower() == "q":
            return TRF.quit_func()
        elif option == '1':
            return metadata_menu()
        elif option == '2':
            return mutations_menu()
        elif option == '3':
            return kegg_menu()
        elif option == '4':
            return goterm_menu()
        elif option == '5':
            return id2gene_menu()
        else:
            print(TRF.invalid_select())
            return simple_process_data_menu()
    exit

def metadata_menu():
    ans = True
    while ans:
        TRF.metadata_menu_text()
        option = input('Select an option: ')
        if option.lower() == 'b':
            return simple_process_data_menu()
        elif option.lower() == 'q':
            return TRF.quit_func()
        elif option == '1':
            return MMF.metadata_menu_opt1_func()
     
        elif option == '2':
            return MMF.metadata_menu_opt2_func()
                
        elif option == '3':
            return MMF.metadata_menu_opt3_func()
                
        elif option == '4':
            return MMF.metadata_menu_opt4_func()
                
        elif option == '5':
            return MMF.metadata_menu_opt5_func()
        
        elif option == '6':
            return MMF.metadata_menu_opt6_func()
        
        elif option == '7':
            return MMF.metadata_menu_opt7_func()
            
        elif option == '8':
            return MMF.metadata_menu_opt8_func()
        
        else:
            print(TRF.invalid_select())
            return metadata_menu()
    exit


def mutations_menu():
    ans = True
    while ans:
        TRF.mutations_menu_text()
        option = input('Select an option: ')
        
        if option.lower() == 'b':
            return simple_process_data_menu()
        elif option.lower() == 'q':
            return TRF.quit_func()
        elif option.lower() == '1':
            return MMF.mutations_menu_opt1_func()
        elif option.lower() == '2':
            return MMF.mutations_menu_opt2_func()
        elif option.lower() == '3':
            return MMF.mutations_menu_opt3_func()
        elif option.lower() == '4':
            return MMF.mutations_menu_opt4_func()
        else:
            print(TRF.invalid_select())
            return mutations_menu()
    exit
        

def kegg_menu():
    ans = True
    while ans:
        TRF.kegg_menu_txt()
        option = input("Select and option: ")
        
        if option.lower() == "b":
            return simple_process_data_menu()

        elif option.lower() == "q":
            return TRF.quit_func()

        elif option.lower() == '1':
            return MMF.kegg_menu_opt1()

        else:
            print(TRF.invalid_select())
            return kegg_menu()
    exit

def goterm_menu():
    ans = True
    while ans:
        TRF.ensid2goterm_menu_txt()
        option = input("Select an option: ")
        
        if option.lower() == 'b':
            return simple_process_data_menu()
        
        elif option.lower() == 'q':
            return TRF.quit_func()
        
        elif option.lower() == '1':
            return MMF.go_terms_menu()
        
        else:
            print(TRF.invalid_select())
            return id2gene_menu()
    exit

def id2gene_menu():
    ans = True
    while ans:
        TRF.id2gene_menu_text()
        option = input("Select an option: ")
        
        if option.lower() == "b":
            return simple_process_data_menu()
       
        elif option.lower() == 'q':
            return TRF.quit_func()

        elif option.lower() == '1':
            return MMF.id2gene_menu_opt1()
        
        elif option.lower() == '2':
            return MMF.id2gene_menu_opt2()

        else:
            print(TRF.invalid_select())
            return id2gene_menu()
    exit

### Main ###
if __name__ == "__main__":
    print(MainMenu())
    
    
### Old code
## Metadata_menu for option 1
#            try:
#                file = input("Enter the name of the file to process: ")
#                return metadata_age(file)
#            except:
#                print("")
#                print('Invalid file name. Please insert the right one.')
#                print('Do not forget to add the file extension at the the end of the file name.')
#                print('Do not forget to check if the file is in the same directory as the program script.')
#                print('Do not forget that it is not necessary to quote the file name.')
#                return metadata_menu()