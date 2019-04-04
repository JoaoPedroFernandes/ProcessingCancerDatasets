# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:35:40 2018

@author: JF
"""

import pandas as pd
import AuxiliaryFunctions as AF
import glob

def read_file(file):
    f = pd.read_table(file)
    return f

def read_csv_file(file):
    f = pd.read_csv(file)
    return f

def stack_column(df):
    f = df.loc[:,('Beta_value','gene_symbol','submitter_id')]
    df = f.drop('gene_symbol', axis=1).join(f['gene_symbol'].str.split(';', expand=True).stack().reset_index(level=1, drop=True).rename('Gene'))
    return df

def trunc_samp_ids(df):
    df['submitter_id'] = df['submitter_id'].map(lambda x: str(x).split('-01')[0])
    return df

def gene_samp_bval(df, pt_cs):
    df['Cancer_Subtype'] = df['submitter_id'].map(pt_cs.set_index('PATIENT_ID')['Cancer_Subtype'])
    del df['submitter_id']
    df = df[['Gene','Cancer_Subtype','Beta_value']]
    return df

def remove_nas(df):
    f = df.dropna(how='any')
    return f

def sub_bval_by_mean(df):
    df['Bval'] = (df.groupby(['Gene','Cancer_Subtype'])['Beta_value'].transform('mean'))
    del df['Beta_value']
    df.rename(columns = {'Bval':'Beta_value'}, inplace = True)
    df = df.drop_duplicates()
    df['Beta_value'] = df['Beta_value'].apply(lambda x: round(x,3))
    df.rename(columns={'Gene':'Hugo_Symbol'}, inplace = True)
    return df


def apply_metprocess_to_all_met_dfs(pt_cs):
    path = AF.read_met_files()
    allFiles = glob.glob(path + "/*.txt")
    frame = pd.DataFrame()
    list_ = []
    for file in allFiles:
        single_met = read_file(file)
        df = stack_column(single_met)
        df = trunc_samp_ids(df)
        df = gene_samp_bval(df, pt_cs)
        df = remove_nas(df)
        df = sub_bval_by_mean(df)
        list_.append(df)
    frame = pd.concat(list_)
    return frame


### Data Reduction ###
def met_data_reduction(met_df, work_genes):
    all_genes = work_genes.iloc[:,0].unique()
    bval_filt = met_df[met_df['Hugo_Symbol'].isin(all_genes)]
    return bval_filt

def write_met_reduct_file(out):
    cwd = AF.write_in_out_dir()
    out.to_csv(cwd+'DR_Gene_Bval.csv', index = False, header = True)

### Main ###
if __name__ == '__main__':
#    single_met = read_file('ABCA12_methylation.data.txt')
#    pt_cs = read_csv_file('pt_cs.csv')
#    df = stack_column(single_met)
#    df = trunc_samp_ids(df)
#    df = gene_samp_bval(df, pt_cs)
#    df = remove_nas(df)
#    df = sub_bval_by_mean(df)
#    print(df)
    
    #pt_cs = read_csv_file('pt_cs.csv')
    #work_genes = read_csv_file('GenesToWork.csv')
    #df = apply_metprocess_to_all_met_dfs_teste(r'C:\Users\Utilizador\Desktop\methylation_tables',pt_cs)
    #out = met_data_reduction(df, work_genes)
    #write_met_reduct_file(out)
    
    
    path = AF.read_met_files()
    allFiles = glob.glob(path + "/*.txt")
    for file in allFiles:
        a = file
    print(read_file(a))