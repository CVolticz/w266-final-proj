import pandas as pd
import os 
import numpy as np
import scipy.stats as st


dir_i = os.getcwd()
file_i = "Metrics_All.csv"

df = pd.read_csv(os.path.join(dir_i,file_i))

genre_dict = {'folk':'Folk','jazz':'Jazz','metal':'Metal','pop':'Pop',
              'rap':'Rap','rb':'R&B','rock':'Rock','soul':'Soul'}
final_summary = []
for i in ['Org','Baseline','LSTM','GPT']:
    for g in ['folk','jazz','metal','pop','rap','rb','rock','soul']:
        for t in ['PAV','SSV','MSV']:
            m_i = df['Model']==i
            m_g = df['Genre']==g
            
            d = df[t]
            d = d[m_i & m_g]
            m = d.mean()
            std = d.std()
            print(i,g,t,len(d.index)); print(d.head(5).to_string())#;input()
            d = d.tolist()
            ci = st.t.interval(alpha=0.95, df=len(d)-1, loc=np.mean(d), scale=st.sem(d)) 
            print(round(m,3))
            print((round(ci[0],3),round(ci[1],3)))
            
            if i == 'Org': i_d = 'Original'
            else: i_d = i
            g_d = genre_dict[g]
            final_summary.append([ i_d,g_d,t,round(m,3),round(std,3) ])

final_summary = pd.DataFrame(final_summary, columns = ['Model','Genre','Type', 'Mean', 'STD'])


file_i = 'Confidence_Interval_Semantics.csv'
final_summary.to_csv(os.path.join(dir_i,file_i),index = False)

