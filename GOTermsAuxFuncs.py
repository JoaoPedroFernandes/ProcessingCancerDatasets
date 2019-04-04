# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:51:06 2018

@author: JF
"""

import requests, sys
import pandas as pd
import numpy as np
import AuxiliaryFunctions as AF

def prepare_ensemblid(file):
    df = pd.read_csv(file)
    res = df.loc[:,'Gene']
    return list(res)

##maybe not needed
#def write_ensemblid_file(df):
#    df.to_csv('ensemblID_list.csv', index= False, header = True)
##maybe not needed
#def open_ensemblid_file(doc):
#    L = []
#    file = open(doc)
#    for line in file.readlines()[1::]:
#        if line == "":
#            pass
#        else:
#            L.append(str(line.split('\n')[0]))
#    return L

def query_godb(file):
    server = "https://rest.ensembl.org"
    res = []
    for gene in file:
        ext = "/xrefs/id/"+gene+"?external_db=GO;all_levels=1"
        r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
        if not r.ok:
            pass
        else:
#            r.raise_for_status()
#            sys.exit()
            decoded = r.json()
            temp = (gene, decoded)
            res.append(temp)
    return res

def get_goID(result):
    L = []
    for lis in result:
        for dic in lis[1]:
            for it in dic.keys():
                if it == "primary_id":
                    temp = str(lis[0]) + ',' + dic[it]
                    L.append(temp)
    return list(sorted(set(L)))

def organize_goids(go_ids_list):
    L, ens_id, go_id = [], [], []
    for val in go_ids_list:
        ens_id.append(val.split(',')[0])
        go_id.append(val.split(',')[1])
    L.append(ens_id)
    L.append(go_id)
    return L

def get_goids_df(L):
    df = pd.DataFrame(L)
    df = df.transpose()
    df.columns = ["EnsembleID","GOterm"]
    return df

def write_ensid_goterm_file(df):
    cwd = AF.write_in_out_dir()
    df.to_csv(cwd+'GOids.csv', index = False, header = True)


### Main ###
if __name__ == '__main__':
    a = prepare_ensemblid('DR_Id2Gene.csv')
    print(a)
    c = query_godb(a)
    d = get_goID(c)
    e = organize_goids(d)
    f = get_goids_df(e)    
    print(f)
#    print(write_ensid_goterm_file(f))


#Old code
#import mygene
#
#mg = mygene.MyGeneInfo()
#
#out = mg.getgene('ENSG00000141510', fields= 'go')
#
#def myprint(d):
#  for k, v in d.items():
#    if isinstance(v, dict):
#      myprint(v)
#    else:
#      return "{0} : {1}".format(k, v)
#
#print(myprint(out))


#gene = str(input("Gene: "))
#server = "https://rest.ensembl.org"
#ext = "/xrefs/id/"+gene+"?external_db=GO;all_levels=1"
#
#r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
#
#if not r.ok:
#  r.raise_for_status()
#  sys.exit()
#
#decoded = r.json()
#
#L = {}
#for dic in decoded:
#    for it in dic.keys():
#        if it == "primary_id":
##            L.append(dic[it])
#            if gene not in L.keys():
#                L[gene] = ''
#            else:
#                L[gene] += dic[it]
#        
#        
#print(L, len(decoded))
##print(list(sorted(set(L))), len(set(L)))
#    for ensem in result:
#        for ens in ensem:
#            for dic in ens:
#                for it in dic.keys():
#                    L.append(it)
##                    if it == "primary_id":
##                        L.append(dic[it])
