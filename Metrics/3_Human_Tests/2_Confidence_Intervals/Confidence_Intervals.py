import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_csv('Human Survey.csv')
lyric_gen_types = list(df['Lyric Type'].unique())

final_summary = []
for l in lyric_gen_types:
    m = df['Lyric Type']==l
    #Human Written	Machine Generated	I Know This Song
    for t in ['Human Written','Machine Generated']:
        df_i = df[t][m]

        
        mean_i = df_i.mean()
        CI = st.t.interval(alpha=0.95, df=len(df_i)-1, loc=np.mean(df_i), scale=st.sem(df_i))
        #print(l,t,mean_i,CI)
        tol = 1
        final_summary.append([l,t,round(mean_i,tol),(round(CI[0],tol),round(CI[1],tol))])
final_summary=pd.DataFrame(final_summary,columns=['Lyric Generation Type','Survey Response','Mean','Confidence Interval'])
print(final_summary.to_string())
final_summary.to_csv('Survey Responses_Confidence_Interval.csv',index=False)




df = pd.read_csv('Human Survey.csv')
lyric_gen_types = list(df['Lyric Type'].unique())

final_summary = []
for l in lyric_gen_types:
    m = df['Lyric Type']==l
    #Human Written	Machine Generated	I Know This Song
    for t in ['Human Written Percent','Machine Generated Percent']:
        df_i = df[t][m]

        
        mean_i = df_i.mean()
        CI = st.t.interval(alpha=0.95, df=len(df_i)-1, loc=np.mean(df_i), scale=st.sem(df_i))
        #print(l,t,mean_i,CI)
        tol = 1
        final_summary.append([l,t,round(mean_i,tol),(round(CI[0],tol),round(CI[1],tol))])
final_summary=pd.DataFrame(final_summary,columns=['Lyric Generation Type','Survey Response','Mean','Confidence Interval'])
print(final_summary.to_string())
final_summary.to_csv('Survey Responses_Confidence_Interval_Percent.csv',index=False)




genre_types = list(df['Genre'].unique())
final_summary = []
for l in lyric_gen_types:
    for g in genre_types:
        m1 = df['Lyric Type']==l
        m2 = df['Genre']==g
        #Human Written	Machine Generated	I Know This Song
        for t in ['Human Written','Machine Generated','I Know This Song']:
            df_i = df[t][m1]
            df_i = df_i[m2]
            #print(df_i);input()
            
            mean_i = df_i.mean()
            CI = st.t.interval(alpha=0.95, df=len(df_i)-1, loc=np.mean(df_i), scale=st.sem(df_i))
            #print(l,t,mean_i,CI)
            tol = 1
            final_summary.append([l,g,t,round(mean_i,tol),(round(CI[0],tol),round(CI[1],tol))])
final_summary=pd.DataFrame(final_summary,columns=['Lyric Generation Type','Genre','Survey Response','Mean','Confidence Interval'])
print(final_summary.to_string())
final_summary.to_csv('Survey Responses_Confidence_Interval_Genre.csv',index=False)
