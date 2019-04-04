# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 04:06:14 2018

@author: JF
"""

import pandas as pd
import ProbsCalculAuxFuncs as AFpc
import JoinAuxiliaryFunctions as JAF
import AuxiliaryFunctions as AF
import Menu as M
import Id2GeneAuxFuncs as AFig
import os
import shutil
import glob

### Get Auxiliary Files Functions ###
#Opt1
def get_pt_cs(file):
    JAF.join_auxfuncs_cs(file)
    


#Opt2
def write_wg_file(df):
    cwd = AF.write_in_out_dir()
    cwd1 = AF.read_input_files()
    df.to_csv(cwd+'GenesToWork.csv', index = False, header = True)
    df.to_csv(cwd1+'GenesToWork.csv', index = False, header = True)


def get_wg(file,pt_cs,val):
    file = AFpc.read_txt_file(file)
    wg = AFpc.read_pt_cs_file(pt_cs)
    occ = AFpc.count_occ(wg)
    df = AFpc.select_features(file)
    df = AFpc.trunc_sampleid(df)
    df = AFpc.merge_2df(df, wg)
    df = AFpc.remove_duplicates(df)
    df = AFpc.cross_table(df)
    df = AFpc.occ_tab_to_df(df)
    df = AFpc.get_prob_crosstab(df,occ)
    df = AFpc.filter_genes(df, val)
    df = AFpc.structure_final_mut_df_dr(df)
    df = df.loc[:,'Hugo_Symbol'].unique()
    df = pd.DataFrame({'Hugo_Symbol':df})
    write_wg_file(df)
    return df

#Opt3
def write_id2gene_file(df):
    cwd = AF.write_in_out_dir()
    cwd1 = AF.read_input_files()
    df.to_csv(cwd+'Id2Gene.csv', index = False, header = True)
    df.to_csv(cwd1+'Id2Gene.csv', index = False, header = True)

def get_id2gene_file(file,wg):
    JAF.join_auxfuncs_id2gene_opt2(file,wg)
    



### Load Input Files Functions ###

def copy_file(filePath):
    AF.create_input_dir()
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Input_Files' 
    try:
        folderPath = os.path.join(cwd, os.path.basename(filePath))
        shutil.copyfile(filePath, folderPath)
    except:
        print('\nPermission denied.\nPlease try again.')
        return M.load_files_menu()



### Load Methylation Files Functions ###
def copy_dir(dirPath):
    allFiles = glob.glob(dirPath+ "/*.txt")
    AF.create_met_dir()
    cwd = os.getcwd()
    cwd = cwd.rsplit(str('\\'),1)[-2]
    cwd = cwd + '\\' + 'Input_Files' + '\\' + 'Methylation_Tables'
    try:
        for f in allFiles:
            shutil.copy(f,cwd)
    except:
        print('\nPermission denied.\nPlease try again.')
        return M.load_files_menu()

if __name__ == '__main__':
#Opt1
#    print(get_pt_cs('samp.txt'))    
#opt2
    #print(get_wg('data_mutations_extended.txt','pt_cs.csv',float(0.50)))

    print(copy_dir(r'C:\Users\Utilizador\Desktop\methylation_tables'))