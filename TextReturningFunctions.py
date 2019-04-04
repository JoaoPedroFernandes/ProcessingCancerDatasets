# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:00:30 2018

@author: JF
"""

import sty as c

### Text Returning Functions ###
# Menus Texts #
def main_menu_text():
    print('''
        
            Main Menu
                    
        1. Help
        2. Actions
        
        q. Quit

        ''')


def submenu_text():
    print('''
        
            Actions Menu
        
        1. Load Input Files
        2. Get Auxiliary Files
        3. Process Data       
        
        b. Back
        q. Quit
        
        ''')

def load_files_menu_text():
    print('''
        
            Load Input Files Menu
        
        1. Load Metadata Input File
        2. Load Mutations Input File
        3. Load Methylations Input File
        4. Load Gene Expression Input File
        5. Load Methylation Input Files

        b. Back
        q. Quit
        
        ''')

def get_files_menu_text():
    print('''
        
            Get Auxiliary Files Menu
        
        1. Patient and it's respective Cancer Subtype
        2. Genes to Work
        3. Ensemble ID to Gene Name
        
        b. Back
        q. Quit
        
        ''')

def process_data_menu_text():
    print('''
        
            Process Data Menu
        
        1. Simple Data Process Menu
        2. Data Associated to Probabilities Calculi Menu       
        
        b. Back
        q. Quit
        
        ''')

def simple_process_data_menu_text():
    print('''
        
            Simple Data Process Menu
        
        1. Metadata
        2. Mutations
        3. KEEG Pathways
        4. GO Terms
        5. ID2Gene
        
        b. Back
        q. Quit
        
        ''')

def associated_probs_calcul_menu_text():
    print('''
        
            Data Associated to Probabilities Calculi Menu 
        
        1. Metadata Associated Probabilities
        2. Gene Mutations Associated Probabilities
        3. Methylation Associated Probabilities
        4. Gene Expression Associated Probabilities
        
        b. Back
        q. Quit
        
        ''')

def associated_probs_metadata_menu_text():
    print('''
        
            Metadata Associated Probabilities 
        
        1. Cancer Subtype + Age + Probability
        
        b. Back
        q. Quit
        
        ''')

def associated_probs_mutations_menu_text():
    print('''
        
            Gene Mutations Associated Probabilities 
        
        1. Mutated Gene + Cancer Subtype + Probability Without Data Dimensionality Reduction
        2. Mutated Gene + Cancer Subtype + Probability With Data Dimensionality Reduction
        
        3. Mutated Gene + Variant Classification + Probability Without Data Dimensionality Reduction
        4. Mutated Gene + Variant Classification + Probability With Data Dimensionality Reduction

        b. Back
        q. Quit
        
        ''')

def associated_probs_methylation_menu_text():
    print('''
        
            Methylation Associated Probabilities
        
        1. Gene + Cancer Subtype + Probability

        b. Back
        q. Quit
        
    ''')

def associated_probs_ge_menu_text():
    print('''
    
            Genetic Expression Menu
        
        1. GEM Data + Cancer Subtype process with data dimensionality reduction
        
        b. Back
        q. Quit
        
    ''')

def metadata_menu_text():
    print('''
        
            Metadata Menu
        
        1. Age
        2. Country
        3. Gender
        4. Lauren Classification
        5. Race
        6. Ethnicity
        7. Cancer Stage
        8. Molecular Subtype (CS)
        
        b. Back
        q. Quit
        
        ''')

def mutations_menu_text():
    print('''
    
            Mutations Menu
        
        1. Patient ID + Mutated Gene + Variant Classification Without Data Dimensionality Reduction 
        2. Patient ID + Mutated Gene + Variant Classification With Data Dimensionality Reduction
        
        3. Patient ID + Mutated Gene Without Data Dimensionality Reduction
        4. Patient ID + Mutated Gene With Data Dimensionality Reduction
        
        b. Back
        q. Quit
                      
    ''')

#'''        NOTE: The "Mutated Gene + Cancer Subtype + Probability" option filters the 
#                  mutations dataset to a low number of genes.
#                  Those are considered the genes to work which would be further used to 
#                  perform data reduction actions.
#              In order to use some other utilities of the program, it is required to
#                  perform this menu action 3 - List of Genes To Work - right after this
#                  menu action 1. This will  generate a csv file with the name of the
#                  genes to work with. 
#              Thank you! 
#    '''



def kegg_menu_txt():
    print('''
    
            KEGG Pathways Menu
        
        1. Gene Name + KEGG Pathways
        
        b. Back
        q. Quit
        
    ''')

def ensid2goterm_menu_txt():
    print('''
    
            EnsemblID 2 GO Term Menu
        
        1. Ensembl ID to Go Term
        
        b. Back
        q. Quit
        
    ''')

def id2gene_menu_text():
    print('''
    
            EnsemblId 2 Gene Name Menu
        
        1. Ensembl ID to Gene without data dimensionality reduction
        2. Ensembl ID to Gene with data dimensionality reduction
        
        b. Back
        q. Quit
        
    ''')


# Other Text Functions #
def help_func():
    a = '''
    Texto a explicar tudo direito.
    Em desenvolvimento ...
    '''
    return a

def quit_func():
    a = '''
    Thank you for using our program.
    Sincerely hope to see you soon.
    Goodbye.
    '''
    return a

def wrong_filename(): # usada quando o ficheiro/df a ser lido nao esta escrito corretamente
    a = c.fg.red +'\n\tInvalid file name. Please insert the right one.' + c.fg.rs
    b = c.fg.red + '\tDo not forget to check if the input file structure is the required one. See details in the option 1 in the Main Menu.' + c.fg.rs
    cc = c.fg.red + '\tDo not forget to add the file extension at the the end of the file name.' + c.fg.rs
    d = c.fg.red + '\tDo not forget to check if the file is in the same directory as the program script.' + c.fg.rs
    e = c.fg.red + '\tDo not forget that it is not necessary to quote the file name.' + c.fg.rs
    f = c.fg.red + '\tOtherwise, the file simply does not exist.' + c.fg.rs
    print(a,b,cc,d,e,f, sep = '\n')


def write_file_feedback(df): # Give a feedback to the user if its desired option waas correctly wroten in a file
    try: # verificar se existe a variável no sistema. Caso n exista, vai para o execpt
        df
        print('\nThe file was successfully processed. Check it yourself!')
    except:
        print('\nThe file was not successfully processed. You can try again!\nIf the error presist, please contact the program adminstrators.')

def invalid_select():
    a = c.fg.red + 'Invalid option selection. Please try again.' + c.fg.rs
    return a


if __name__ == "__main__":
    pass