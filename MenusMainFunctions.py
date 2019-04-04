# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:16:37 2018

@author: JF
"""

import os.path

import Menu as M
import AuxiliaryFunctions as AF
import TextReturningFunctions as TRF
import JoinAuxiliaryFunctions as JAF
import OtherMenuFunctions as OMF

### All Menus Functions ###

#### Main Menu FUnctions ###
def main_menu_func():
    try:
        option = input('Select an option: ')
        if option == '1':
            print(TRF.help_func())
            print('\n\n')
            return AF.back_or_quit()
        elif option == '2':
            return M.submenu()
        elif option == 'q':
            return TRF.quit_func()
        else:
            print('Invalid option! Please select a number from 1-2 or "q" to quit the program.')
            return M.MainMenu()
    except ValueError:
        print('Invalid option! Please select a number from 1-2 or "q" to quit the program.')


### Sub Menu Functions ###
def submenu_func():
    option = input('Select an option: ')
    if option.lower() == 'b':
        return M.MainMenu()
    elif option.lower() == "q":
        return TRF.quit_func()
    elif option.lower() == '1':
        return M.load_files_menu()
    elif option.lower() == '2':
        return M.get_files_menu()
    elif option.lower() == '3':
        return M.process_data_menu()
    else:
        print(TRF.invalid_select())
        return M.submenu()

### Get Files Menu ###
#Opt1
def get_files_menu_opt1_func():
    file = AF.read_input_files() + str(input('Enter the metadata file name to process in order to get the pt_cs file (Patient ID + Cancer Subtype): '))
    if os.path.exists(file):
        AF.waiting_message()
        try:
            final = OMF.get_pt_cs(file)
            TRF.write_file_feedback(final)
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        TRF.wrong_filename()
        return M.get_files_menu()
        
#Opt2
def get_files_menu_opt2_func():
    file = AF.read_input_files() + str(input('Enter the name of the mutations file: '))
    if os.path.exists(file):
        wg = AF.read_input_files() + str(input('Enter the name of the file that contains the Patient ID + Cancer Subtype: '))
        if os.path.exists(wg):
            try:
                val = float(input('Enter the value (float) which is going to be use to perform the data dimensionality reduction: '))
            except:
                print('\nInvalid value.\n Please select a float between 0.0 and 1.0')
                return M.get_files_menu()
            if float(val) >= float(0.0) and float(val) <= float(1.0):
                AF.waiting_message()
                try:
                    final = OMF.get_wg(file,wg,val)
                    TRF.write_file_feedback(final)
                    return AF.back_or_quit()
                except:
                    print('\nWrong file or structure file. Please, read the help menu and try again.')
                    return M.MainMenu()
            else:
                print('\nInvalid value.\n Please select a float between 0.0 and 1.0')
                return M.get_files_menu()
        else:
            TRF.wrong_filename()
            return M.get_files_menu()
    else:
        TRF.wrong_filename()
        return M.get_files_menu()

#Opt3
def get_files_menu_opt3_func():
    file = AF.read_input_files() + str(input('Enter the mutations file name to process in order to get the Id2Gene file (EnsemblID + Hugo_Symbol): '))
    if os.path.exists(file):
        wg = AF.read_input_files() + str(input('Enter the name of the file that cointains the genes names to reduct: '))
        if os.path.exists(wg):
            AF.waiting_message()
            try:            
                final = OMF.get_id2gene_file(file,wg)
                TRF.write_file_feedback(final)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else:
            TRF.wrong_filename()
            return M.get_files_menu()
    else:
        TRF.wrong_filename()
        return M.get_files_menu()


### Load Input Files Menu Functions ###
#Opt1, Opt2, Opt3 and Opt4
def load_input_files_menu_func():
    path = str(input('Enter the entire path of the file to be loaded into the the program as an input file: '))
    if os.path.exists(path):
        AF.waiting_message()
        try:
            OMF.copy_file(path)
            print('\nThe file was successfully loaded into the program.')
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        print('\nIt was impossible to load the file into the program.')
        print('Invalid file name or invalid path.')
        print('Please try again.')
        return M.load_files_menu()

#Opt 5 (methylation)
def load_input_files_menu_opt5_func():
    path =  str(input('Enter the entire path of the methylation files to be loaded into the the program as input files: '))
    if os.path.exists(path):
        AF.waiting_message()
        try:
            OMF.copy_dir(path)
            print('\nThe files were successfully loaded into the program.')
            return AF.back_or_quit()
        except:
            print('\nWrong file(s) or structure file(s). Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        print('\nIt was impossible to load the files into the program.')
        print('Invalid path.')
        print('Please try again.')
        return M.load_files_menu()

### Process Data Menu Function ###
def process_data_menu_func():
    option = input('Select an option: ')
    if option.lower() == 'b':
        return M.submenu()
    elif option.lower() == "q":
        return TRF.quit_func()
    elif option == '1':
        return M.simple_process_data_menu()
    elif option == '2':
        return M.associated_probs_calcul_menu()
    else:
        print(TRF.invalid_select())
        return M.process_data_menu()

### Associated Probabilities Calculi Menu Function ###
def associated_probs_calcul_menu_func():
    option = input('Select an option: ')
    if option.lower() == 'b':
        return M.process_data_menu()
    elif option.lower() == "q":
        return TRF.quit_func()
    elif option.lower() == '1':
        return M.metadata_associated_prob_menu()
    elif option.lower() == '2':
        return M.mut_associated_prob_menu()
    elif option.lower() == '3':
        return M.met_associated_prob_menu()
    elif option.lower() == '4':
        return M.genetic_expression_associated_prob_menu()
    else:
        print(TRF.invalid_select())
        return M.associated_probs_calcul_menu()

##### Simple Data Process Menu Functions #####    
### Metadata Menu Functions ###
# Age
def metadata_menu_opt1_func():
    file = AF.read_input_files() + input("Enter the name of the file to process: ")
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_age(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()

# Country    
def metadata_menu_opt2_func():
    file = AF.read_input_files() + str(input("Enter the name of the file to process: "))
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_country(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()

# Gender
def metadata_menu_opt3_func():
    file = AF.read_input_files() + str(input("Enter the name of the file to process: "))
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_gender(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()

# Lauren Classification
def metadata_menu_opt4_func():
    file = AF.read_input_files() + str(input("Enter the name of the file to process: "))
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_lc(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()

# Race
def metadata_menu_opt5_func():
    file = AF.read_input_files() + str(input("Enter the name of the file to process: "))
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_race(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()

# Ethnicity
def metadata_menu_opt6_func():
    file = AF.read_input_files() + str(input("Enter the name of the file to process: "))
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_et(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()

# Stage
def metadata_menu_opt7_func():
    file = AF.read_input_files() + str(input("Enter the name of the file to process: "))
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_stage(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()

# Molecular/Cancer Subtype
def metadata_menu_opt8_func():
    file = AF.read_input_files() + str(input("Enter the name of the file to process: "))
    if os.path.exists(file) == True:   
        AF.waiting_message()
        try:             
            final = JAF.join_auxfuncs_cs(file)
            TRF.write_file_feedback(final) # sem o 'print' para não aparecer o None no output
            return AF.back_or_quit()
        except:
            print('Error.\nPlease verify if your file as the right column(s) to process. See the Help menu to more details.')
            return M.metadata_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_menu()


### Mutations Menu Functions ###
# Opt1
def mut_opt1(file):
    final = JAF.join_auxfuncs_mut_opt1(file)
    return TRF.write_file_feedback(final)

def mutations_menu_opt1_func():
    file = AF.read_input_files() + str(input("Enter the name of the mutations file to process: "))
    if os.path.exists(file):
        AF.waiting_message()
        try:
            mut_opt1(file)
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        TRF.wrong_filename()
        return M.mutations_menu()

#Opt2
def mut_opt2(file, wg):
    final = JAF.join_auxfuncs_mut_opt2(file,wg)
    return TRF.write_file_feedback(final)

def mutations_menu_opt2_func():
    file1 = AF.read_input_files() + str(input("Enter the name of the mutations file to process: "))
    if os.path.exists(file1):
        file2 = AF.read_input_files() + str(input("Enter the file that contains the gene names to work with: " ))
        if os.path.exists(file2):
            AF.waiting_message()
            try:
                mut_opt2(file1,file2)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else:
            TRF.wrong_filename()
            return M.mutations_menu()
    else:
        TRF.wrong_filename()
        return M.mutations_menu()
        
# Opt3
def mut_opt3(file):
    final = JAF.join_auxfuncs_mut_opt3(file)
    return TRF.write_file_feedback(final)

def mutations_menu_opt3_func():
    file = AF.read_input_files() + str(input("Enter the name of the mutations file to process: "))
    if os.path.exists(file):
        AF.waiting_message()
        try:
            mut_opt3(file)
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        TRF.wrong_filename()
        return M.mutations_menu()

# Opt4
def mut_opt4(file, wg):
    final = JAF.join_auxfuncs_mut_opt4(file,wg)
    return TRF.write_file_feedback(final)

def mutations_menu_opt4_func():
    file1 = AF.read_input_files() + str(input("Enter the name of the mutations file to process: "))
    if os.path.exists(file1):
        file2 = AF.read_input_files() + str(input("Enter the file that contains the gene names to work with: " ))
        if os.path.exists(file2):
            AF.waiting_message()
            try:
                mut_opt4(file1,file2)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else:
            TRF.wrong_filename()
            return M.mutations_menu()
    else:
        TRF.wrong_filename()
        return M.mutations_menu()


### KEGG Menu Functions   ###
def kegg_paths(file):
    final = JAF.join_aux_funcs_keeg(file)
    return TRF.write_file_feedback(final)

def kegg_menu_opt1():
    file = AF.read_input_files() + str(input("Enter the name of the file with the name of genes (one by line) to get the respectives KEGG Pathways: "))
    if os.path.exists(file):
        AF.waiting_message()
        try:
            kegg_paths(file)
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        TRF.wrong_filename()
        return M.kegg_menu()

### GO Terms Menu Functions ###
def go_terms(file):
    final = JAF.join_auxfuncs_ensid2go_opt1(file)
    return TRF.write_file_feedback(final)

def go_terms_menu():
    file = AF.read_input_files() + str(input("Enter the name of the id2gene to get the respectives GO Terms ID's: "))
    if os.path.exists(file):
        AF.waiting_message()
        try:
            go_terms(file)
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        TRF.wrong_filename()
        return M.goterm_menu()

### Id2Gene Menu Functions ###
def id2gene_process_opt1(file):
    final = JAF.join_auxfuncs_id2gene_opt1(file)
    return TRF.write_file_feedback(final)

def id2gene_menu_opt1():
    f1 = AF.read_input_files() + str(input("Enter the name of the mutations file to process: "))
    if os.path.exists(f1):
        AF.waiting_message()
        try:
            id2gene_process_opt1(f1)
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        TRF.wrong_filename()
        return M.id2gene_menu()

def id2gene_process_opt2(f1,f2):
    final = JAF.join_auxfuncs_id2gene_opt2(f1,f2)
    return TRF.write_file_feedback(final)

def id2gene_menu_opt2():
    f1 = AF.read_input_files() + str(input("Enter the name of the mutations file to process: "))
    if os.path.exists(f1):
        f2 = AF.read_input_files() + str(input("Enter the name of the file that contains the list of genes to work with: ")) 
        if os.path.exists(f2):
            AF.waiting_message()
            try:
                id2gene_process_opt2(f1,f2)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else:
            TRF.wrong_filename()
            return M.id2gene_menu()
    else:
        TRF.wrong_filename()
        return M.id2gene_menu()

##### Associated Probability Calcul Menu Functions #####
## Mutations
#Opt1
def prob_mut_opt1(file, wg):
    final = JAF.join_auxfuncs_prob_mut_opt1(file, wg)
    return TRF.write_file_feedback(final)

def prob_mutations_menu_opt1_func():
    file = AF.read_input_files() + str(input('Enter the name of the mutations file to process: '))
    if os.path.exists(file):
        wg = AF.read_input_files() + str(input('Enter the name of the file that contains the Patient ID + Cancer Subtype: '))
        if os.path.exists(wg):
            AF.waiting_message()
            try:
                prob_mut_opt1(file, wg)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else: 
            TRF.wrong_filename()
            return M.mut_associated_prob_menu()
    else:
        TRF.wrong_filename()
        return M.mut_associated_prob_menu()

#Opt2
def prob_mut_opt2(file, wg, val):
    final = JAF.join_auxfuncs_prob_mut_opt2(file, wg, val)
    return TRF.write_file_feedback(final)

def prob_mutations_menu_opt2_func():
    file = AF.read_input_files() + str(input('Enter the name of the mutations file to process: '))
    if os.path.exists(file):
        wg = AF.read_input_files() + str(input('Enter the name of the file that contains the Patient ID + Cancer Subtype: '))
        if os.path.exists(wg):
            try:
                val = float(input('Enter the value (float) which is going to be use to perform the data dimensionality reduction: '))
            except:
                print('\nInvalid value.\n Please select a float between 0.0 and 1.0')
                return M.mut_associated_prob_menu()
            if float(val) >= float(0.0) and float(val) <= float(1.0):
                AF.waiting_message()
                try:
                    prob_mut_opt2(file, wg, val)
                    return AF.back_or_quit()
                except:
                    print('\nWrong file or structure file. Please, read the help menu and try again.')
                    return M.MainMenu()
            else:
                print('\nInvalid value.\n Please select a float between 0.0 and 100.0')
                return M.mut_associated_prob_menu()
        else:
            TRF.wrong_filename()
            return M.mut_associated_prob_menu()
    else:
        TRF.wrong_filename()
        return M.mut_associated_prob_menu()

#Opt3
def prob_mut_opt3(file):
    final = JAF.join_auxfuncs_prob_mut_opt3(file)
    return TRF.write_file_feedback(final)

def prob_mutations_menu_opt3_func():
    file = AF.read_input_files() + str(input('Enter the name of the mutations file to process: '))
    if os.path.exists(file):
        AF.waiting_message()
        try:
            prob_mut_opt3(file)
            return AF.back_or_quit()
        except:
            print('\nWrong file or structure file. Please, read the help menu and try again.')
            return M.MainMenu()
    else:
        TRF.wrong_filename()
        return M.mut_associated_prob_menu()

#Opt4
def prob_mut_opt4(file,wg):
    final = JAF.join_auxfuncs_prob_mut_opt4(file,wg)
    return TRF.write_file_feedback(final)

def prob_mutations_menu_opt4_func():
    file = AF.read_input_files() + str(input('Enter the name of the mutations file to process: '))
    if os.path.exists(file):
        wg = AF.read_input_files() + str(input('Enter the name of the file that contains the genes names to work with: '))
        if os.path.exists(wg):
            AF.waiting_message()
            try:
                prob_mut_opt4(file,wg)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else:
            TRF.wrong_filename()
            return M.mut_associated_prob_menu()
    else:
        TRF.wrong_filename()
        return M.mut_associated_prob_menu()

### Metadata ###
#Opt Age + Cs + Prob #
def prob_metadata_opt1(file,pt_cs):
    final = JAF.join_auxfuncs_prob_metadata_opt1(file,pt_cs)
    return TRF.write_file_feedback(final)

def prob_metadata_menu_opt1_func():
    file = AF.read_input_files() + str(input('Enter the name of the patient metadata file to process: '))
    if os.path.exists(file):
        pt_cs = AF.read_input_files() + str(input('Enter the name of the file that maps a patient to its respective cancer subtype: '))
        if os.path.exists(pt_cs):
            AF.waiting_message()
            try:
                prob_metadata_opt1(file,pt_cs)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else:
            TRF.wrong_filename()
            return M.metadata_associated_prob_menu()
    else:
        TRF.wrong_filename()
        return M.metadata_associated_prob_menu()

### Methylation ###
# Met Opt1
def prob_bval_met(f1,f2):
    final = JAF.join_auxfuncs_prob_met_opt1(f1,f2)
    return TRF.write_file_feedback(final)

def prob_methylation_menu_opt1_func():
    f1 = AF.read_input_files() + str(input("Enter the name of the file matches each patient to its repective cancer subtype: "))
    if os.path.exists(f1):
        f2 = AF.read_input_files() + str(input("Enter the name of the file that cointains the genes names to reduct: "))
        if os.path.exists(f2):
            AF.waiting_message()
            try:
                prob_bval_met(f1,f2)
                return AF.back_or_quit()
            except:
                print('\nWrong file or structure file. Please, read the help menu and try again.')
                return M.MainMenu()
        else:
            TRF.wrong_filename()
            return M.met_associated_prob_menu()
    else:
        TRF.wrong_filename()
        return M.met_associated_prob_menu()


### Genetic Expression Menu Functions ###
#GenExp Opt1
def prob_gem_cs_process_reduct(file, wg, ig, pt_cs):
    final = JAF.join_auxfuncs_prob_ge_opt1(file,wg,ig,pt_cs)
    return TRF.write_file_feedback(final)

def prob_genexp_menu_opt1_func():
    f1 = AF.read_input_files() + str(input("Enter the name of the original gene expression matrix (GEM) to process: "))
    if os.path.exists(f1):
        f2 = AF.read_input_files() + str(input("Enter the name of the file which contains the gene names to filter the GEM: "))
        if os.path.exists(f2):
            f3 = AF.read_input_files() + str(input("Enter the name of the file which makes the match betwen the gene Ensmbl ID and its repective symbol: "))
            if os.path.exists(f3):
                f4 = AF.read_input_files() + str(input("Enter the name of the file that matches each patient to its repective cancer subtype: "))
                if os.path.exists(f4):
                    AF.waiting_message()
                    try:
                        prob_gem_cs_process_reduct(f1,f2,f3,f4)
                        return AF.back_or_quit()
                    except:
                        print('\nWrong file or structure file. Please, read the help menu and try again.')
                        return M.MainMenu()
                else:
                    TRF.wrong_filename()
                    return M.genetic_expression_associated_prob_menu()
            else:
                TRF.wrong_filename()
                return M.genetic_expression_associated_prob_menu()
        else:
            TRF.wrong_filename()
            return M.genetic_expression_associated_prob_menu()
    else:
        TRF.wrong_filename()
        return M.genetic_expression_associated_prob_menu()


if __name__ == "__main__":
    pass