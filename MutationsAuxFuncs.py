# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:39:47 2018

@author: JF
"""

import pandas as pd

import AuxiliaryFunctions as AF

# Mutations - Simple data process #
#Opt1
def read_txt_file(file):
    df = pd.read_table(file)
    return df

def select_mutgene_features(df):
    df = df.loc[:,('Tumor_Sample_Barcode','Hugo_Symbol','Variant_Classification')]
    return df

def trunc_tumor_ids(df):
     df['Tumor_Sample_Barcode'] = df['Tumor_Sample_Barcode'].map(lambda x: str(x).split("-01-")[0])
     df['Variant_Classification'] = df.loc[:,'Variant_Classification'].str.lower()
     return df

def remove_duplicates(df):
    df = df.drop_duplicates(subset=['Tumor_Sample_Barcode','Hugo_Symbol','Variant_Classification'])
    return df

def transform_vc_nas(df):
    v = df['Variant_Classification'].value_counts().argmax()
    df.loc[:,'Variant_Classification'] = df.loc[:,'Variant_Classification'].fillna(v)
    return df

def process_vc_col(df):
    df['Variant_Classification'] = df['Variant_Classification'].str.replace("'","")
    return df
    
def write_pt_gene_mutclass(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_gene_mutclass.csv', index = False, header = True)


#Opt2
def select_pt_gene_features_gs(df):
    df = df.loc[:,('Tumor_Sample_Barcode','Hugo_Symbol')]
    return df

def trunc_tumor_ids_gs(df):
     df['Tumor_Sample_Barcode'] = df['Tumor_Sample_Barcode'].map(lambda x: str(x).split("-01-")[0])
     return df

def remove_duplicates_gs(df):
    df = df.drop_duplicates(subset=['Tumor_Sample_Barcode','Hugo_Symbol'])
    return df

def write_pt_mutgene(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_mutgene.csv', index = False, header = True)


# Data Reduction - Applies to all options #
def read_wg_file(file):
    wg = pd.read_csv(file)
    return wg

def mut_data_reduct(df, wg):
    filt_genes = wg.iloc[:,0]
    filt = df[df['Hugo_Symbol'].isin(filt_genes)]
    filt.reset_index(level = 0, inplace = True)
    filt.pop('index')    
    return filt

def write_pt_gene_mutclass_dr(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'DR_pt_gene_mutclass.csv', index = False, header = True)

def write_pt_mutgene_dr(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'DR_pt_mutgene.csv', index = False, header = True)



### Main ###
if __name__ == '__main__':
    #Opt1     
#     #file = read_txt_file('data_mutations_extended.txt')     #244065
#     out = select_mutgene_features(file)
#     out = trunc_tumor_ids(out)
#     out = remove_duplicates(out)                             #225130
#     out = transform_vc_nas(out) 
#     out = process_vc_col(out)
#     wg = read_wg_file('GenesToWork.csv')
#     out = mut_data_reduct(out,wg)                            #13139 (17% reducted)
#     print(out)

    #Opt2
#    file = read_txt_file('data_mutations_extended.txt')
    out = select_pt_gene_features_gs(file)
    out = trunc_tumor_ids_gs(out)
    out = remove_duplicates_gs(out)
    wg = read_wg_file('GenesToWork.csv')
    out = mut_data_reduct(out, wg)
    print(out)