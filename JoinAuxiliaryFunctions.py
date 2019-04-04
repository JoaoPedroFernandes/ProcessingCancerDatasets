# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:37:22 2018

@author: JF
"""
import pandas as pd

import AuxiliaryFunctions as AF
import MutationsAuxFuncs as AFmut
import MetadataAuxFuncs as AFmeta
import KEGGPathwaysAuxFuncs as AFkegg
import Id2GeneAuxFuncs as AFig
import MethylationAuxFuncs as AFmet
import GeneticExpressionAuxFuncs as AFge
import GOTermsAuxFuncs as AFgo
import ProbsCalculAuxFuncs as AFpc

###### Simple Data Process ######
### Mutations ###
# Opt1
def join_auxfuncs_mut_opt1(file):
    df = AFmut.read_txt_file(file)
    df = AFmut.select_mutgene_features(df)
    df = AFmut.trunc_tumor_ids(df)
    df = AFmut.remove_duplicates(df)
    df = AFmut.transform_vc_nas(df) 
    df = AFmut.process_vc_col(df)
    AFmut.write_pt_gene_mutclass(df)

def join_auxfuncs_mut_opt2(file, work_g):
    df = AFmut.read_txt_file(file)
    wg = AFmut.read_wg_file(work_g)
    df = AFmut.select_mutgene_features(df)
    df = AFmut.trunc_tumor_ids(df)
    df = AFmut.remove_duplicates(df)
    df = AFmut.transform_vc_nas(df) 
    df = AFmut.process_vc_col(df)
    df = AFmut.mut_data_reduct(df,wg)
    AFmut.write_pt_gene_mutclass_dr(df)

def join_auxfuncs_mut_opt3(file):
    df = AFmut.read_txt_file(file)
    df = AFmut.select_pt_gene_features_gs(df)
    df = AFmut.trunc_tumor_ids_gs(df)
    df = AFmut.remove_duplicates_gs(df)
    AFmut.write_pt_mutgene(df)
    
def join_auxfuncs_mut_opt4(file, work_g):
    df = AFmut.read_txt_file(file)
    wg = AFmut.read_wg_file(work_g)
    df = AFmut.select_pt_gene_features_gs(df)
    df = AFmut.trunc_tumor_ids_gs(df)
    df = AFmut.remove_duplicates_gs(df)
    df = AFmut.mut_data_reduct(df,wg)
    AFmut.write_pt_mutgene_dr(df)


### Metadata ###
# Metadata Age #
def join_auxfuncs_age(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_age_features(df)
    df = AFmeta.transform_age_nas(df)
    AFmeta.write_pt_age(df)


# Metadata Country #
def join_auxfuncs_country(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_country_features(df)
    df = AFmeta.transform_country_nas(df)
    AFmeta.write_pt_country(df)

    
# Metadata Gender #
def join_auxfuncs_gender(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_gender_features(df)
    df = AFmeta.transform_gender_nas(df)
    AFmeta.write_pt_gender(df)


# Metadata Lauren Classification #
def join_auxfuncs_lc(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_lc_features(df)
    df = AFmeta.transform_lc_nas(df)
    AFmeta.write_pt_lc(df)

# Metadata Race #
def join_auxfuncs_race(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_race_features(df)
    df = AFmeta.transform_race_nas(df)
    AFmeta.write_pt_race(df)

# Metadata Ethnicity #
def join_auxfuncs_et(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_et_features(df)
    df = AFmeta.transform_et_nas(df)
    AFmeta.write_pt_et(df)

# Metadata Stage #
def join_auxfuncs_stage(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_stage_features(df)
    df = AFmeta.transform_stage_nas(df)
    AFmeta.write_pt_stage(df)
    
# Metadata Molecular/Cancer Subtype #
def join_auxfuncs_cs(file):
    file = AFmeta.read_file(file)
    df = AFmeta.trunc_pat_ids(file)
    df = AFmeta.select_cs_features(df)
    df = AFmeta.transform_cs_nas(df)
    AFmeta.write_pt_cs(df)



### KEEG Pathways ###
def join_aux_funcs_keeg(file):
    genes = AFkegg.open_file(file)
    genes_list = AFkegg.get_pathway(genes)
    AFkegg.fileToKB(genes_list)




### EnsemblID2GOterm ###
def join_auxfuncs_ensid2go_opt1(file):
    a = AFgo.prepare_ensemblid(file)
    b = AFgo.query_godb(a)
    c = AFgo.get_goID(b)
    d = AFgo.organize_goids(c)
    e = AFgo.get_goids_df(d)
    AFgo.write_ensid_goterm_file(e)



### Id2Gene ###
def join_auxfuncs_id2gene_opt1(file):
    id2gene = AFig.read_file(file)
    all_genes = AFig.select_features(id2gene)
    out = AFig.remove_duplicated_noreducted(all_genes)
    AFig.write_id2gene_file(out)

def join_auxfuncs_id2gene_opt2(file, work_genes):
    id2gene = AFig.read_file(file)
    work_genes = AFig.read_work_genes(work_genes)
    all_genes = AFig.select_features(id2gene)
    out = AFig.non_duplicates_genes(all_genes,work_genes)
    AFig.write_id2_gene_datareduct(out)





###### Associated Probabilities Data Calculi Process #####
### Mutations ###
#Opt1
def join_auxfuncs_prob_mut_opt1(file, pt_cs):
    pt_cs = AFpc.read_pt_cs_file(pt_cs)
    occ = AFpc.count_occ(pt_cs)
    file = AFpc.read_txt_file(file)
    df = AFpc.select_features(file)
    df = AFpc.trunc_sampleid(df)
    df = AFpc.merge_2df(df, pt_cs)
    df = AFpc.remove_duplicates(df)
    df = AFpc.cross_table(df)
    df = AFpc.occ_tab_to_df(df)
    df = AFpc.get_prob_crosstab(df,occ)
    df = AFpc.structure_final_mut_df(df)
    AFpc.write_gene_cs_prob_file(df)

#Opt2
def join_auxfuncs_prob_mut_opt2(file,pt_cs,val):
    pt_cs = AFpc.read_pt_cs_file(pt_cs)
    occ = AFpc.count_occ(pt_cs)
    file = AFpc.read_txt_file(file)
    df = AFpc.select_features(file)
    df = AFpc.trunc_sampleid(df)
    df = AFpc.merge_2df(df, pt_cs)
    df = AFpc.remove_duplicates(df)
    df = AFpc.cross_table(df)
    df = AFpc.occ_tab_to_df(df)
    df = AFpc.get_prob_crosstab(df,occ)
    df = AFpc.filter_genes(df, val)     # val dado no input (codigo em MMF modulo)
    df = AFpc.structure_final_mut_df_dr(df)
    AFpc.write_gene_cs_prob_file_dr(df)

#Opt3
def join_auxfuncs_prob_mut_opt3(file):
    file = AFpc.read_txt_file(file)
    df = AFpc.select_features_opt34(file)                         #244065
    df = AFpc.trunc_sampleid_opt34(df)
    df = AFpc.remove_duplicates_opt34(df)                         #225130
    df = AFpc.transform_vc_nas(df)
    df = AFpc.process_vc_col(df)
    df = AFpc.remove_undesired_values(df)                         #225049
    df = AFpc.get_probs_opt34(df)                                 #70630
    df = AFpc.remove_dates_opt34(df)                              #70539
    AFpc.write_gene_vc_prob(df)

#Opt4
def join_auxfuncs_prob_mut_opt4(file,wg):
    file = AFpc.read_txt_file(file)
    wg = AFpc.read_wg_file(wg)
    df = AFpc.select_features_opt34(file)                         #244065
    df = AFpc.trunc_sampleid_opt34(df)
    df = AFpc.remove_duplicates_opt34(df)                         #225130
    df = AFpc.transform_vc_nas(df)
    df = AFpc.process_vc_col(df)
    df = AFpc.remove_undesired_values(df)                         #225049
    df = AFpc.get_probs_opt34(df)                                 #70630
    df = AFpc.remove_dates_opt34(df)                              #70539  
    df = AFpc.mut_data_reduct_opt34(df, wg)                       #1338
    AFpc.write_gene_vc_prob_dr(df)
    

### Metadata ###
#Opt Age + Cs + Prob #
def join_auxfuncs_prob_metadata_opt1(file,pt_cs):
    file = AFpc.read_met_file(file)
    pt_cs = AFpc.read_pt_cs_file(pt_cs)
    df = AFpc.trunc_met_pat_ids(file)
    df = AFpc.select_age_features(df)
    df = AFpc.transform_age_nas(df)
    df = AFpc.merge_2df(df,pt_cs)
    mean_cs = AFpc.get_cs_age_mean(df)
    std_cs = AFpc.get_cs_age_std(df)    
    df = AFpc.repeat_cs(df)
    df = AFpc.get_all_probs(df,mean_cs,std_cs)
    AFpc.write_cs_age_prob_file(df)


### Methylation ###
def join_auxfuncs_prob_met_opt1(f1 = 'pt_cs.csv', f2 = 'GenesToWork.csv'):
    pt_cs = AFmet.read_csv_file(f1)
    work_genes = AFmet.read_csv_file(f2)
    df = AFmet.apply_metprocess_to_all_met_dfs(pt_cs)
    out = AFmet.met_data_reduction(df, work_genes)
    AFmet.write_met_reduct_file(out)

### Gene Expression ###
def join_auxfuncs_prob_ge_opt1(f1, f2 = "GenesToWork.csv", f3 = "DR_Id2Gene.csv", f4='pt_cs.csv'):
    file = AFge.read_fpkm_file(f1)
    work_genes = AFge.read_csv_file(f2)
    id2gene = AFge.read_csv_file(f3)
    pt_cs = AFge.read_csv_file(f4)
    df= AFge.trunc_geneID(file)
    df = AFge.data_reduct(df,work_genes,id2gene)
    df_t = AFge.express_transpose(df)
    dfs_l = AFge.split_original_df_nr(df_t)
    out = AFge.process_cs_GEM(dfs_l, pt_cs)
    out = AFge.concat_dfs(out)
    AFge.write_genexp_cs_reduct_file(out)


if __name__ == '__main__':
#    file = AFpc.read_txt_file('data_mutations_extended.txt')
#    wg = AFpc.read_wg_file('pt_cs.csv')
#    occ = AFpc.count_occ(wg)
#    df = AFpc.select_features(file)
#    df = AFpc.trunc_sampleid(df)
#    df = AFpc.merge_2df(df, wg)
#    df = AFpc.remove_duplicates(df)
#    df = AFpc.cross_table(df)
#    df = AFpc.occ_tab_to_df(df)
#    df = AFpc.get_prob_crosstab(df,occ)
#    val = float(input('Enter treshold value: '))
#    df = AFpc.filter_genes(df, val)     # val dado no input (codigo em MMF modulo)
#    df = AFpc.structure_final_mut_df_dr(df)
#    print(df)

#Metadata
    join_auxfuncs_prob_metadata_opt1('p.txt','pt_cs.csv')