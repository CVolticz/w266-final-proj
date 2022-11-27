import pandas as pd
# import relevant libraries
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

#Org
for g in  ['soul','jazz','folk','pop','metal','rb','rock','rap']:
    final_metric_list = []
    final_metric_df = pd.read_csv(f"Metrics_{g}.csv")
    
    final_metric_df['Model']="Org"
    final_metric_df['Genre']=g
    results[f"{g}_Org"] = final_metric_df[final_cols]

#Baseline
model='Baseline'
final_cols = ['Model','Genre','lyrics','PAV','SSV','MSV']
for g in  ['soul','jazz','folk','pop','metal','rb','rock','rap']:
    final_metric_list = []
    final_metric_df = pd.read_csv(f"Metrics_{model}_{g}.csv")
    
    final_metric_df['Model']=model
    final_metric_df['Genre']=g
    results[f"{g}_{model}"] = final_metric_df[final_cols]
  
#LSTM
model='lstm_attention'
for g in  ['soul','jazz','folk','pop','metal','rb','rock','rap']:
    
    if g=='rb': lyrics_name = 'R&B'
    else:       lyrics_name = g.capitalize()
    
    final_metric_list = []
    final_metric_df = pd.read_csv(f"{model}_{g}_generated_lyrics.csv")
    
    final_metric_df['lyrics']=final_metric_df[lyrics_name]
    final_metric_df['Model']="LSTM"
    final_metric_df['Genre']=g
    results[f"{g}_LSTM"] = final_metric_df[final_cols]

#GPT
model='GPT'
for g in  ['soul','jazz','folk','pop','metal','rb','rock','rap']:
    final_metric_list = []
    final_metric_df = pd.read_csv(f"{model}_{g}_generated_lyrics.csv")
    
    final_metric_df['lyrics']=final_metric_df['generated_lyric']
    final_metric_df['Model']=model
    final_metric_df['Genre']=g    
    results[f"{g}_{model}"] = final_metric_df[final_cols]

#Combine all and save
df_list = []
for k in results.keys():
    df_list.append(results[k])
df_list = pd.concat(df_list)
df_list.to_csv('Metrics_All.csv')
