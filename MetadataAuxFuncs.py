# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 11:57:59 2018

@author: JF
"""

import pandas as pd
import numpy as np

import AuxiliaryFunctions as AF



def read_file(file):
    df = pd.read_table(file)
    new_header = df.iloc[3] #grab the first row for the header
    df = df[4:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    df = df.reset_index()
    df = df.iloc[:,1::]
    return df

def trunc_pat_ids(df):
    df['PATIENT_ID'] = df['PATIENT_ID'].map(lambda x: str(x).split('-01')[0])
    return df

# Age
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

def write_pt_age(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_age.csv', index = False, header = True)

# Country
def select_country_features(df):
    if 'COUNTRY_OF_PROCUREMENT' in df.columns:
        df = df.loc[:,('PATIENT_ID','COUNTRY_OF_PROCUREMENT')]
        df.rename(columns={'COUNTRY_OF_PROCUREMENT':'COUNTRY'}, inplace = True)
        df['COUNTRY'] = df['COUNTRY'].str.lower()
        return df
    else:
        return 'The COUNTRY column is not in the dataframe or it is not named COUNTRY_OF_PROCUREMENT.'

def transform_country_nas(df):
    v = df['COUNTRY'].value_counts().argmax()
    df.loc[:,'COUNTRY']=df.loc[:,'COUNTRY'].fillna(v)    
    return df
    
def write_pt_country(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_country.csv', header = True, index = False)
 
# Gender
def select_gender_features(df):
    if 'GENDER' in df.columns:
        df = df.loc[:,('PATIENT_ID','GENDER')]
        df['GENDER'] = df['GENDER'].str.lower()
        return df
    else:
        print('The GENDER column is not in the dataframe or it is not named GENDER.')

def transform_gender_nas(df):
    v = df['GENDER'].value_counts().argmax()
    df.loc[:,'GENDER'] = df.loc[:,'GENDER'].fillna(v)
    return df

def write_pt_gender(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_gender.csv', index = False, header = True)

# Lauren Classification
def select_lc_features(df):
    if 'LAUREN_CLASS' in df.columns:
        df = df.loc[:,('PATIENT_ID','LAUREN_CLASS')]
        df['LAUREN_CLASS'] = df['LAUREN_CLASS'].str.lower()
        return df
    else:
        print('The LAUREN_CLASS is not in the dataframe or it is not named LAUREN_CLASS.')

def transform_lc_nas(df):
    v = df['LAUREN_CLASS'].value_counts().argmax()
    df.loc[:,'LAUREN_CLASS'] = df.loc[:,'LAUREN_CLASS'].fillna(v)
    return df

def write_pt_lc(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_lc.csv', index = False, header = True)

# Race
def select_race_features(df):
    if 'RACE' in df.columns:
        df = df.loc[:,('PATIENT_ID','RACE')]
        df['RACE'] = df['RACE'].str.lower()
        return df
    else:
        print('The RACE column is not in the dataframe or it is not named RACE.')

def transform_race_nas(df):
    v = df['RACE'].value_counts().argmax()
    df.loc[:,'RACE'] = df.loc[:,'RACE'].fillna(v)
    return df

def write_pt_race(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_race.csv', index = False, header = True)

# Ethnicity
def select_et_features(df):
    if 'ETHNICITY' in df.columns:
        df = df.loc[:,('PATIENT_ID','ETHNICITY')]
        df['ETHNICITY'] = df['ETHNICITY'].str.lower()
        return df
    else:
        print('The ETHNICITY column is not in the dataframe or it is not named ETHNICITY.')

def transform_et_nas(df):
    v = df['ETHNICITY'].value_counts().argmax()
    df.loc[:,'ETHNICITY'] = df.loc[:,'ETHNICITY'].fillna(v)
    return df

def write_pt_et(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_ethnicity.csv', index = False, header = False)

# Stage
def select_stage_features(df):
    if 'TNMSTAGE' in df.columns:
        df = df.loc[:,('PATIENT_ID','TNMSTAGE')]
        df['TNMSTAGE'] = df['TNMSTAGE'].str.lower()
        return df
    else:
        print('The TNMSTAGE column is not in the dataframe or it is not namet TNMSTAGE.')

def transform_stage_nas(df):
    v = df['TNMSTAGE'].value_counts().argmax()
    df.loc[:,'TNMSTAGE'] = df.loc[:,'TNMSTAGE'].fillna(v)
    df.rename(columns={'TNMSTAGE':'Cancer_Stage'}, inplace = True)
    return df

def write_pt_stage(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'pt_stage.csv', index = False, header = True)

# Molecular/Cancer Subtype
def select_cs_features(df):
    if 'MOLECULAR_SUBTYPE' in df.columns:
        df = df.loc[:,('PATIENT_ID','MOLECULAR_SUBTYPE')]
        df['MOLECULAR_SUBTYPE'] = df['MOLECULAR_SUBTYPE'].str.lower()
        return df
    elif 'SUBTYPE' in df.columns:
        df = df.loc[:,('PATIENT_ID','SUBTYPE')]
        df['SUBTYPE'] = df['SUBTYPE'].str.lower()
        return df
    else:
        print('The MOLECULAR_SUBTYPE or the SUBTYPE column are not in the dataframe or they are not named MOLECULAR_SUBTYPE and SUBTYPE, repectively.')

def transform_cs_nas(df):
    if 'MOLECULAR_SUBTYPE' in df.columns:
        v = df['MOLECULAR_SUBTYPE'].value_counts().argmax()
        df.loc[:,'MOLECULAR_SUBTYPE'] = df.loc[:,'MOLECULAR_SUBTYPE'].fillna(v)
        return df
    elif 'SUBTYPE' in df.columns:
        v = df['SUBTYPE'].value_counts().argmax()
        df.loc[:,'SUBTYPE'] = df.loc[:,'SUBTYPE'].fillna(v)
        return df
    else:
        print('The MOLECULAR_SUBTYPE or the SUBTYPE column are not in the dataframe or they are not named MOLECULAR_SUBTYPE and SUBTYPE, repectively.')

def write_pt_cs(df):
    cwd = AF.write_in_out_dir()
    cwd1 = AF.read_input_files()
    if 'MOLECULAR_SUBTYPE' in df.columns:
        df.rename(columns={'MOLECULAR_SUBTYPE':'Cancer_Subtype'}, inplace = True)
        df.to_csv(cwd+'pt_cs.csv', index = False, header = True)
        df.to_csv(cwd1+'pt_cs.csv', index = False, header = True)
    elif 'SUBTYPE' in df.columns:
        df.rename(columns={'SUBTYPE':'Cancer_Subtype'}, inplace = True)
        df.to_csv(cwd+'pt_cs.csv', index = False, header = True)
        df.to_csv(cwd1+'pt_cs.csv', index = False, header = True)
    else:
        print('The MOLECULAR_SUBTYPE or the SUBTYPE column are not in the dataframe or they are not named MOLECULAR_SUBTYPE and SUBTYPE, repectively.')
 


### Auxiliary Genetic Expression Functions ###

### Auxiliary Methylation Functions ###

### Auxiliary Mutations Functions ###

### Auxiliary Mutated Gene + Cs + Prob Functions ###

### Auxiliary KEEG Pathways Functions ###

### Auxiliary GO Terms Functions ###

### Auxiliary ID2Gene Functions ###





### Main ###
if __name__ == "__main__":
    pass