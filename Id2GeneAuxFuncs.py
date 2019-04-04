# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:45:40 2018

@author: JF
"""

import pandas as pd
import AuxiliaryFunctions as AF

def read_file(file):
    df1 = pd.read_table(file)
    return df1

def read_work_genes(work_genes):
    df2 = pd.read_csv(work_genes)
    return df2

def select_features(file):
    df = file.loc[:,('Gene','Hugo_Symbol')]
    return df

def remove_duplicated_noreducted(c):
    df = c.drop_duplicates(subset = ['Gene','Hugo_Symbol'])
    out = df[df.Gene != 'HYDIN']
    return out
    
def non_duplicates_genes(c, b):
    all_genes = b.iloc[:,0].unique()   #ficar apenas com os genes não repetidos
    all_genes_id = c[c['Hugo_Symbol'].isin(all_genes)]
    gene_ids = all_genes_id.iloc[:,0].unique()
    id2gene_filt = all_genes_id[all_genes_id['Gene'].isin(gene_ids)].drop_duplicates()
    return id2gene_filt


def write_id2gene_file(out):
    cwd = AF.write_in_out_dir()
    cwd1 = AF.read_input_files()
    out.to_csv(cwd+'Id2Gene.csv', index = False, header = True)
    out.to_csv(cwd1+'Id2Gene.csv', index = False, header = True)

def write_id2_gene_datareduct(out):
    cwd = AF.write_in_out_dir()
    cwd1 = AF.read_input_files()
    out.to_csv(cwd+'DR_Id2Gene.csv', index = False, header = True)
    out.to_csv(cwd1+'DR_Id2Gene.csv', index = False, header = True)



if __name__ == "__main__":
    file = read_file('data_mutations_extended.txt')
    #wg = read_work_genes('GenesToWork.csv')
    #df = select_features(file)
    #out = non_duplicates_genes(df,wg)
    #print(out)
    a = select_features(file)
    print(a)