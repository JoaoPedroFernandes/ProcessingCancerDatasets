# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 02:37:24 2018

@author: JF
"""

import pandas as pd
import numpy as np
import AuxiliaryFunctions as AF



def read_fpkm_file(file):
    df = pd.read_table(file)
    return df

def read_csv_file(file):
    f = pd.read_csv(file)
    return f

def trunc_geneID(df):
    df.rename(columns = {df.columns[0]: 'Ensemble_ID'}, inplace = True)
    df['Ensemble_ID'] = df['Ensemble_ID'].apply(lambda x: x.split('.')[0])
    return df

def index(df):
    df.set_index('Ensemble_ID', inplace = True)
    return df

def express_transpose(df):
    out = index(df)
    out = out.T
    out.index.names = ['Sample']
    return out

def split_original_df_nr(df):
    outdflist =[]
    for i, col in enumerate(df):
        # create a subdf with desired columns:
        subdf = df[[col]]
        # append subdf to list of df: 
        outdflist.append(subdf)
    return outdflist

def concat_dfs(dfs):
    all_dfs = pd.concat(dfs, join='inner')
    return all_dfs

### Data Reduction Function ###

def data_reduct(df,work_genes,id2gene):
    all_genes = work_genes.iloc[:,0].unique()
    all_genes_id = id2gene[id2gene['Hugo_Symbol'].isin(all_genes)]
    gene_ids = all_genes_id.iloc[:,0].unique()
    expression_filt = df[df['Ensemble_ID'].isin(gene_ids)]
    return expression_filt
    


############# Genetic Expression by CS ##############
def asso_cs(df, pt_cs):
    df.reset_index(level=0, inplace = True)
    df.index.name = None
    df['Sample'] = df['Sample'].apply(lambda x: x.split('-01')[0])
    df['Sample'] = df['Sample'].apply(lambda x: x.split('-11')[0])
    df['Cancer_Subtype'] = df['Sample'].map(pt_cs.set_index('PATIENT_ID')['Cancer_Subtype'])
    return df


def order(df):
    df.drop('Sample',axis = 1, inplace = True)
    df.dropna(inplace=True)
    return df

def add_cs_exppro_col(df):
    df['Exp_prof']  = pd.cut(df.iloc[:,0], bins = [0,1,10,100,np.inf],
                                    labels = ['low_exp','norm_exp','high_exp','very_high_exp'])
    df['Exp_prof'] = df['Exp_prof'].cat.add_categories(['non_exp'])
    df['Exp_prof'] = df['Exp_prof'].fillna('non_exp')
    return df


def add_cs_probval_col(df):
    occ = df.groupby('Cancer_Subtype')['Exp_prof'].value_counts()/df.groupby('Cancer_Subtype')['Exp_prof'].count()
    occ = pd.DataFrame(occ.reset_index(name='Expression_Probability'))
    return occ

def re_order_col(df):
    df = df[['Ensembl_ID','Cancer_Subtype','Exp_prof','Expression_Probability']]
    df.Expression_Probability = df.Expression_Probability.round(3)
    return df

def process_cs_GEM(dfs, pt_cs):
    L = []
    for df in dfs:
        asso_cs(df, pt_cs)
        order(df)
        add_cs_exppro_col(df)
        name = df.columns[0]
        out_df = add_cs_probval_col(df)
        out_df['Ensembl_ID'] = name
        out_df = re_order_col(out_df)
        L.append(out_df)
    return L
    

def write_genexp_cs_reduct_file(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'DR_GeneExpression_cs.csv',index=False,header=True)




if __name__ == '__main__':
    ###### No Data Reduction ######
#    file = read_fpkm_file('STAD.fpkm.txt')
#    dfs = trunc_geneID(file)w
#    dfs = split_original_df_nr(dfs)
#    dfs = add_exppro_col_nr(dfs)
#    out = concat_dfs_nr(dfs)
#    print(out)
    
    ###### With Data Reduction   ######
#    file = read_fpkm_file('STAD.fpkm.txt')
#    work_genes = read_csv_file('GenesToWork.csv')
#    id2gene = read_csv_file('Id2Gene_filtrated.csv')
#    df = trunc_geneID(file)
#    data_reducted = data_reduct(df,work_genes, id2gene)
#    trans = express_transpose(data_reducted)
#    dfs = split_original_df(trans)
#    dfs = process_GEM(dfs)
#    print(dfs[14])
#    out = concat_dfs(dfs)
#    print(out)

# Genetic Expression by CS #
#    file = read_fpkm_file('STAD.fpkm.txt')
#    work_genes = read_csv_file('GenesToWork.csv')
#    id2gene = read_csv_file('DR_Id2Gene.csv')
#    pt_cs = read_csv_file('pt_cs.csv')
    df= trunc_geneID(file)
    df = data_reduct(df,work_genes,id2gene)
    df_t = express_transpose(df)
    dfs_l = split_original_df_nr(df_t)
#    out = process_cs_GEM(dfs_l, pt_cs)
#    out = concat_dfs(out)
#    print(out)
    a = asso_cs(dfs_l[1], pt_cs)
    b = order(a)
    c = add_cs_exppro_col(b)
    name = c.columns[0]
    d = add_cs_probval_col(c)
    d['Ensembl_ID'] = name
    e = re_order_col(d)
    print(c.groupby('Cancer_Subtype')['Exp_prof'].value_counts())
    print('\n\n\n')
    print(c.groupby('Cancer_Subtype')['Exp_prof'].count())

