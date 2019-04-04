# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:43:23 2018

@author: JF
"""

import pandas as pd
import numpy as np
import AuxiliaryFunctions as AF



# Geral Functions # 
def read_txt_file(file):
    df = pd.read_table(file)
    return df

def read_pt_cs_file(file):
    wg = pd.read_csv(file)
    return wg

def read_wg_file(file):
    wg = pd.read_csv(file)
    wg.rename(columns={'Genes':'Hugo_Symbol'}, inplace = True)
    return wg

### Mutations ###
## Opt1 and Opt2
def select_features(df):
    df = df.loc[:,('Hugo_Symbol','Tumor_Sample_Barcode')]
    return df

def trunc_sampleid(df):
    df['Tumor_Sample_Barcode'] = df['Tumor_Sample_Barcode'].map(lambda x: str(x).split("-01")[0])
    df.rename(columns={'Tumor_Sample_Barcode':'PATIENT_ID'}, inplace = True)
    return df

def merge_2df(pt_gene,pt_cs):
    df = pt_gene.merge(pt_cs, on = 'PATIENT_ID', how = 'inner')
    return df

def remove_duplicates(df):
    df = df.drop_duplicates(['Hugo_Symbol','PATIENT_ID'])
    return df
    
def cross_table(df):
    for_crosstab = df.iloc[:,(0,2)]
    occ = pd.crosstab(for_crosstab.Hugo_Symbol,for_crosstab.Cancer_Subtype)
    return occ


def count_occ(occ):
    occ = occ.rename(columns={ occ.columns[1]: "Cancer_Subtype" })
    out = occ.loc[:,'Cancer_Subtype'].value_counts()
    return out.to_dict()

def occ_tab_to_df(occ):
    df = pd.DataFrame(occ)
    return df

def get_prob_crosstab(df, occ):
    for col in df.columns:
        df[col] = df[col]/occ[col]
    return df
    

def structure_final_mut_df(filt):
    outfile = pd.melt(filt.reset_index(), id_vars=filt.index.name)
    outfile = outfile.replace(0.0,0.0001)
    outfile.rename(columns={'value':'Probability'}, inplace = True)
    return outfile

def write_gene_cs_prob_file(outfile):
    cwd = AF.write_in_out_dir()
    outfile.to_csv(cwd+'mutgene_cs_prob.csv', index = False, header = True)

# Data Reduction
def filter_genes(out,val):
    filt = out[out > val].dropna(how = 'all')
    filt_genes = filt.index
    filt = out[out.index.isin(filt_genes)]
    filt.reset_index(level = 0, inplace = True)
    return filt

def structure_final_mut_df_dr(filt):
    outfile = pd.melt(filt, id_vars=['Hugo_Symbol'])
    outfile = outfile.replace(0.0,0.0001)
    outfile.rename(columns={'value':'Probability'}, inplace = True)
    return outfile

    
def write_gene_cs_prob_file_dr(outfile):
    cwd = AF.write_in_out_dir()
    outfile.to_csv(cwd+'DR_mutgene_cs_prob.csv', index = False, header = True)


## Opt3 and Opt4
def select_features_opt34(df):
    df = df.loc[:,('Tumor_Sample_Barcode','Hugo_Symbol','Variant_Classification')]
    return df

def trunc_sampleid_opt34(df):
     df['Tumor_Sample_Barcode'] = df['Tumor_Sample_Barcode'].map(lambda x: str(x).split("-01-")[0])
     df['Variant_Classification'] = df.loc[:,'Variant_Classification'].str.lower()
     return df

def remove_duplicates_opt34(df):
    df = df.drop_duplicates(subset=['Tumor_Sample_Barcode','Hugo_Symbol','Variant_Classification'])
    return df

def transform_vc_nas(df):
    v = df['Variant_Classification'].value_counts().argmax()
    df.loc[:,'Variant_Classification'] = df.loc[:,'Variant_Classification'].fillna(v)
    return df

def process_vc_col(df):
    df['Variant_Classification'] = df['Variant_Classification'].str.replace("'","")
    return df
    
def remove_undesired_values(df):
    df = df[~df['Hugo_Symbol'].isin(['Unknown','HYDIN']) ]
    return df

def get_probs_opt34(df):
    df = df.loc[:,('Hugo_Symbol','Variant_Classification')]
    df = df.groupby(["Hugo_Symbol", "Variant_Classification"]).size().reset_index(name="Frequency")
    df['Total_Frequency'] = df.groupby('Hugo_Symbol')['Frequency'].transform('sum')
    df['Probability'] = df['Frequency'] / df['Total_Frequency']
    df = df.loc[:,('Hugo_Symbol','Variant_Classification','Probability')]
    return df

def remove_dates_opt34(df):
    import re
    pad = '^[0-9]+' + '-' + '[A-Z]'
    r = re.compile(pad)
    a = df[~df.Hugo_Symbol.apply(lambda x: bool(r.match(x)))]
    return a

def write_gene_vc_prob(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'mutgene_vc_prob.csv', index = False, header = True)

#Data Reduction
def mut_data_reduct_opt34(df, wg):
    df = df[df['Hugo_Symbol'].isin(wg.loc[:,'Hugo_Symbol'])]
    return df

def write_gene_vc_prob_dr(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'DR_mutgene_vc_prob.csv', index = False, header = True)



### Metadata ###
#Opt Age + Cs + Prob #
def read_met_file(file):
    df = pd.read_table(file)
    new_header = df.iloc[3] #grab the first row for the header
    df = df[4:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    df = df.reset_index()
    df =  df.iloc[:,1::]
    return df


def trunc_met_pat_ids(df):
    df['PATIENT_ID'] = df['PATIENT_ID'].map(lambda x: str(x).split('-01')[0])
    return df

def select_age_features(df):
    if 'AGE' in df.columns:
        df = df.loc[:,('PATIENT_ID','AGE')]
        return df
    else:
        return 'The AGE column is not in the dataframe or it is not named AGE.'

def transform_age_nas(df):
    df['AGE'] = df['AGE'].apply(pd.to_numeric)
    noNa= df.dropna()
    m = np.mean(noNa.iloc[:,1])
    df.loc[:,'AGE']= df.loc[:,'AGE'].fillna(m).astype(np.int)
    return(df)

def get_cs_age_mean(df):
    mean_df = df.groupby('Cancer_Subtype', as_index=False)['AGE'].mean()
    mean_dict = mean_df.set_index('Cancer_Subtype')['AGE'].to_dict()
    return mean_dict

def get_cs_age_std(df):
    mean_df = df.groupby('Cancer_Subtype')['AGE'].std()
    std_dict = mean_df.to_dict()
    return std_dict

def repeat_cs(df):
    df['Cancer_Subtype'] = df['Cancer_Subtype'].astype('category')
    res = df.groupby(['PATIENT_ID', 'Cancer_Subtype']).first().reset_index()
    res['AGE'] = res.groupby('PATIENT_ID')['AGE'].transform('first').astype(int)
    return res
    
def get_all_probs(df,am,astd):
    df = df.loc[:,('Cancer_Subtype','AGE')]    
    df['Probability'] = df.apply(lambda x: get_cs_age_prob(x['Cancer_Subtype'], x['AGE'],am,astd), axis=1)
    df = df.drop_duplicates(subset=['Cancer_Subtype','AGE'], keep="first")
    return df

def get_cs_age_prob(cs,age,am,astd):
    prob = (1/(np.sqrt(2*3.14*(astd[cs]**2))))*(np.exp(-(((age-am[cs])**2)/(2*(astd[cs]**2)))))
    return prob

def write_cs_age_prob_file(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'cs_age_prob.csv', index = False, header = True)
    
    
    
### Main ###
if __name__ == '__main__':
#Opt1 and Opt2
#    file = read_txt_file('data_mutations_extended.txt')
#    wg = read_pt_cs_file('pt_cs.csv')
#    occ = count_occ(wg)
#    df = select_features(file)
#    df = trunc_sampleid(df)
#    df = merge_2df(df, wg)                                  #244065
#    df = remove_duplicates(df)                              #204513
#    df = cross_table(df)
#    df = occ_tab_to_df(df)
#    df = get_prob_crosstab(df,occ)
#    df = filter_genes(df, 0.50)
#    df = structure_final_mut_df_dr(df)
#    print(df)
#Opt3 and Opt4
#    file = read_txt_file('data_mutations_extended.txt')
#    wg = read_wg_file('GenesToWork.csv')
#    df = select_features_opt34(file)                         #244065
#    df = trunc_sampleid_opt34(df)
#    df = remove_duplicates_opt34(df)                         #225130
#    df = transform_vc_nas(df)
#    df = process_vc_col(df)
#    df = remove_undesired_values(df)                         #225049
#    df = get_probs_opt34(df)                                 #70630
#    df = remove_dates_opt34(df)                              #70539  
#    df = mut_data_reduct_opt34(df, wg)                       #1338
#    print(df)
#Metadata
    file = read_met_file('pat.txt')
    pt_cs = read_pt_cs_file('pt_cs.csv')
    df = trunc_met_pat_ids(file)
    df = select_age_features(df)
    df = transform_age_nas(df)
    df = merge_2df(df,pt_cs)
    mean_cs = get_cs_age_mean(df)
    std_cs = get_cs_age_std(df)    
    df = repeat_cs(df)
    df = get_all_probs(df,mean_cs,std_cs)
    print(df)

#TCGA-BR-4191,72,msi,0.03990434422338111
#TCGA-BR-4191,72,cin,0.02450564358671636
#TCGA-BR-4191,72,gs,0.018273730414947693
#TCGA-BR-4191,72,ebv,0.024154627118760826
