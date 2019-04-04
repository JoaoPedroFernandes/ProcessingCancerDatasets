# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 04:18:05 2018

@author: JF
"""

import pandas as pd
import AuxiliaryFunctions as AF

from bioservices import QuickGO
from mygene import *
from bioservices.kegg import KEGG


#mg = MyGeneInfo()
#print(mg.get_fields("refseq"))

k = KEGG()


def open_file(doc):
    L = []
    file = open(doc)
    for line in file.readlines():
        if line == "":
            pass
        else:
            L.append(str(line.split('\n')[0]))
    return(L)


def get_pathway(doc):
    dic = {}
#    gene_list = open_file(doc)
    for gene in range(len(doc)):
        if doc[gene] != None:
            try:
                pathways = k.get_pathway_by_gene(doc[gene],"hsa")
                if pathways != None:
                    for val in pathways.values():  
                        dic.setdefault(doc[gene], []).append(val.replace("'",""))
            except:
                pass
    return(dic)


def fileToKB(a):
    cwd = AF.write_in_out_dir()
    file = open(cwd+"kegg.csv","w")
    for key in a:
        for value in a[key]: 
            file.write('{},{}\n'.format(str(key),str(value)))
    file.close()





if __name__ == "__main__":
    #print(csv2txt('GenesToWork.csv'))
    print(open_file('genelist.txt'))
    print(get_pathway('GenesToWork.csv'))
    #print(fileToKB(get_pathway('genelist.txt')))
