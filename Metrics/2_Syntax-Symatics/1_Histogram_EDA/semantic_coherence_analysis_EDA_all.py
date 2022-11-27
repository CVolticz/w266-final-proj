import pandas as pd
import re
import random
import joblib
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tqdm.notebook import tqdm
import networkx as nx

import matplotlib.pyplot as plt

#Collect Data frm Org, Baseline, LSTM, GPT
results={}
final_cols = ['Model','Genre','lyrics','PAV','SSV','MSV']
final_metric_df = pd.read_csv(f"Metrics_All.csv")

#Organize Results
genre_list = ['soul','jazz','folk','pop','metal','rb','rock','rap']
for model in ['Org','Baseline','LSTM','GPT']:
    for g in genre_list:
        final_metric_df_i = final_metric_df[final_metric_df['Model']==model]
        final_metric_df_i = final_metric_df_i[final_metric_df_i['Genre']==g]
        results[f"{g}_{model}"] = final_metric_df_i[final_cols]


scale_i = 1.5
b = [e for e in np.linspace(0,1,50)] #25
mult_plots = True
print('Done Reading')


############
#Mult Plots#
############
i=0
for g in genre_list:
    j=0
    fig, axes = plt.subplots(nrows=1, ncols=3)
    fig.set_size_inches(15.5*scale_i, 18.5/7.0)
    for t in ['PAV', 'SSV', 'MSV']:
        for m in ['Org','Baseline','LSTM','GPT']:
            key = g+"_"+m
            df = results[key]
            
            d = df[t]; d = d.rename(m) 
             
            d.hist(ax=axes[j],bins=b, density=True, alpha = 0.5,legend=True) 
            axes[j].set_title( f"{g.capitalize()} {t}" )
        j=j+1
    fig.tight_layout(pad=2.0)
    plt.savefig(f"Semantic Coherence Histograms_{g}.jpeg")
    i=i+1

##########
#One Plot#   
##########
fig, axes = plt.subplots(nrows=len(genre_list), ncols=3)
fig.set_size_inches(15.5*scale_i, 18.5*scale_i)
i=0
for g in genre_list:
    j=0
    for t in ['PAV', 'SSV', 'MSV']:
        for m in ['Org','Baseline','LSTM','GPT']:
            key = g+"_"+m
            df = results[key]
            
            d = df[t]; d = d.rename(m) 
            d.hist(ax=axes[i,j],bins=b, density=True, alpha = 0.5,legend=True)
            axes[i,j].set_title( f"{g.capitalize()} {t}" )
        
        j=j+1
    i=i+1
fig.tight_layout(pad=5.0)
plt.savefig('Semantic Coherence Histograms.jpeg')
#plt.show()    

#####################
#One Plot All Genres#   
#####################
scale_i = 0.75
fig, axes = plt.subplots(nrows=2, ncols=3)
fig.set_size_inches(12.5*scale_i, 18.5*scale_i/3.0)
i=0; lim_dict={}
for t in ['PAV', 'SSV', 'MSV']: lim_dict[t]=0
for m in ['Org','Baseline','LSTM','GPT']:
    j=0
    for t in ['PAV', 'SSV', 'MSV']:
        df_all = []
        for g in genre_list:
            key = g+"_"+m
            df = results[key]
            df_all.append(df)
        df = pd.concat(df_all)
        
        d = df[t]; d = d.rename(m) 
        if m == 'Org': d = d.rename('Original')
        print(i,j)
        d.hist(ax=axes[i,j],bins=b, density=True, alpha = 0.5,legend=True)
        if m == 'Org': d.hist(ax=axes[i+1,j],bins=b, density=True, alpha = 0,legend=False)
        axes[i,j].set_title( f"{t}" )    
        l = axes[i,j].get_ylim()[1]
        lim_dict[t]=max(l,lim_dict[t])
        
        j=j+1; 
    if m == 'Org': i=i+1
#Fix limits
for i in range(2):
    j=0
    for t in ['PAV', 'SSV', 'MSV']:
        l = axes[i,j].set_ylim(0,lim_dict[t])
        print(l)
        j=j+1
plt.suptitle('Semantic Coherence Histograms \n Grouped by Lyric Type and Metric')
fig.tight_layout(pad=1.0)

plt.savefig('Semantic Coherence Histograms Combined Genres.jpeg')
input()

##############
#One Plot Org#  
##############
print('Here')
fig, axes = plt.subplots(nrows=1, ncols=3)
scale_i=1
fig.set_size_inches(12.5*scale_i, 18.5*scale_i/3.0)

i=0; ij= 0
for g in genre_list:
    j=0
    for t in ['PAV', 'SSV', 'MSV']:
        for m in ['Org']:
            key = g+"_"+m
            df = results[key]
            
            d = df[t]; d = d.rename(g) 
            #d.hist(ax=axes[ij,j],bins=b, density=True, alpha = 0.2,legend=True)
            #if ij == 0: axes[ij,j].set_title( f"{t}" )
            d.hist(ax=axes[j],bins=b, density=True, alpha = 0.2,legend=True)
            axes[j].set_title( f"{t}" )
        j=j+1
    i=i+1
    #if i == 2 or i == 4 or i == 6: ij=ij+1
    if i == 4 : ij=ij+1
fig.tight_layout(pad=5.0)
plt.suptitle('Human Dataset Semantic Coherence Histograms')
plt.savefig('Org Semantic Coherence Histograms.jpeg')
#plt.show()    
print('Done')

