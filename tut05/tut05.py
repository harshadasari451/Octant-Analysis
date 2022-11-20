import pandas as pd
import math

from datetime import datetime
start_time = datetime.now()

def octant_range_names(mod=5000):
     try:
        df = pd.read_excel("octant_input.xlsx")  # reading the input file
        df.head()
        df["U_Average"] = df["U"].mean()     
        df["V_Average"] = df["V"].mean()
        df["W_Average"] = df["W"].mean()
        df["U1"] = df["U"]-df["U_Average"]  
        df["V2"] = df["V"]-df["V_Average"] 
        df["W3"] = df["W"]-df["W_Average"] 
        
        df.loc[((df.U1 > 0) & (df.V2 > 0) & (df.W3 >0)), "Octant"] = "+1" 
        df.loc[((df.U1 > 0) &(df.V2 > 0) & (df.W3 <0)), "Octant" ] = "-1"
        df.loc[((df.U1 < 0) &(df.V2 > 0) & (df.W3 >0)), "Octant" ] = "+2"
        df.loc[((df.U1 < 0) &(df.V2 > 0) & (df.W3 <0)), "Octant" ] = "-2"    
        df.loc[((df.U1 < 0) &(df.V2 < 0) & (df.W3 >0)), "Octant" ] = "+3"
        df.loc[((df.U1 < 0) &(df.V2 < 0) & (df.W3 <0)), "Octant" ] = "-3"
        df.loc[((df.U1 > 0) &(df.V2 < 0) & (df.W3 >0)), "Octant" ] = "+4"
        df.loc[((df.U1 > 0) &(df.V2 < 0) & (df.W3 <0)), "Octant" ] = "-4"
        
        x =df['Octant'].value_counts() # total count of number of values for each octant

        df.loc[0,"octant id"]="overall count" 
        df.loc[0,"+1"]=x["+1"]               
        df.loc[0,"-1"]=x["-1"]
        df.loc[0,"+2"]=x["+2"] 
        df.loc[0,"-2"]=x["-2"]
        df.loc[0,"+3"]=x["+3"]
        df.loc[0,"-3"]=x["-3"]
        df.loc[0,"+4"]=x["+4"]
        df.loc[0,"-4"]=x["-4"]
        y=str(mod)
        df.loc[1,"octant id"]="mod"+" "+y 
        try: 
          d=math.ceil(29745/mod) 
          l=0000
          m=mod-1
          a=str(l)
          b=str(m)
          for j in range(d) :
             if int(b)>=29744:
                df.loc[j+2,"octant id"]= a+"-"+"29744"
                l=m+1
                m=m+mod
                a=str(l)
                b=str(m)
             else:
                df.loc[j+2,"octant id"]= a+"-"+b
                l=m+1
                m=m+mod
                a=str(l)
                b=str(m)
          
          c=0 
          t=0
          p=2
          for j in range(d) : # no of coloumns in the output for each octant 
              for i in range(mod) : #running at each 5000 iterations (0-5000,5001-10000,......25000-30000)
                  if df["Octant"][t]=="+4" : # counting number of +4 octant in range of 0-30000
                     c =c+1
                  t=t+1
                  if t== 29745 :  
                    break
              df.loc[p,"+4"]=c #assigning count of +4 in each coloumn by iterating p
              p=p+1
              c=0
              j=7
######################################################################
#repating the above loop###############################
          c=0
          t=0
          p=2
          for j in range(d) :
              for i in range(mod) :
                  if df["Octant"][t]=="-4" :
                     c =c+1
                  t=t+1
                  if t== 29745 :
                    break
              df.loc[p,"-4"]=c 
              p=p+1
              c=0
              j=7
############################################################
          c=0
          t=0
          p=2
          for j in range(d) :
              for i in range(mod) :
                  if df["Octant"][t]=="+3" :
                     c =c+1
                  t=t+1
                  if t== 29745 :
                    break
              df.loc[p,"+3"]=c 
              p=p+1
              c=0
              j=7
######################################################################
          c=0
          t=0
          p=2
          for j in range(d) :
              for i in range(mod) :
                  if df["Octant"][t]=="-3" :
                     c =c+1
                  t=t+1
                  if t== 29745 :
                    break
              df.loc[p,"-3"]=c 
              p=p+1
              c=0
              j=7
############################################################################
          c=0
          t=0
          p=2
          for j in range(d) :
              for i in range(mod) :
                  if df["Octant"][t]=="+2" :
                     c =c+1
                  t=t+1
                  if t== 29745 :
                    break
              df.loc[p,"+2"]=c 
              p=p+1
              c=0
              j=7 
######################################################################
          c=0
          t=0
          p=2
          for j in range(d) :
              for i in range(mod) :
                  if df["Octant"][t]=="-2" :
                     c =c+1
                  t=t+1
                  if t== 29745 :
                    break
              df.loc[p,"-2"]=c 
              p=p+1
              c=0
              j=7
###############################################################
          c=0
          t=0
          p=2
          for j in range(d) :
              for i in range(mod) :
                  if df["Octant"][t]=="+1" :
                     c =c+1
                  t=t+1
                  if t== 29745 :
                    break
              df.loc[p,"+1"]=c
              p=p+1
              c=0
              j=7  
################################################  
          c=0
          t=0
          p=2
          for j in range(d) :
              for i in range(mod) :
                  if df["Octant"][t]=="-1" :
                     c =c+1
                  t=t+1
                  if t== 29745 :
                    break
              df.loc[p,"-1"]=c 
              p=p+1
              c=0
              j=7
          a=[]
          b=[]
          c=[]
          for i in range(8) : 
              c.append(0)
          a.append(df["+1"][0])
          a.append(df["-1"][0])
          a.append(df["+2"][0])
          a.append(df["-2"][0])
          a.append(df["+3"][0])
          a.append(df["-3"][0])
          a.append(df["+4"][0])
          a.append(df["-4"][0])
          b.append(df["+1"][0])
          b.append(df["-1"][0])
          b.append(df["+2"][0])
          b.append(df["-2"][0])
          b.append(df["+3"][0])
          b.append(df["-3"][0])
          b.append(df["+4"][0])
          b.append(df["-4"][0])
          b.sort(reverse = True)
          for i in range(8) : 
              for j in range(8) : 
                  if a[j]==b[i] :
                      c[j]=i+1
                      j=9
          df.loc[0,"rank of +1"]=c[0]                 
          df.loc[0,"rank of -1"]=c[1]                 
          df.loc[0,"rank of +2"]=c[2]
          df.loc[0,"rank of -2"]=c[3]
          df.loc[0,"rank of +3"]=c[4]
          df.loc[0,"rank of -3"]=c[5]
          df.loc[0,"rank of +4"]=c[6]
          df.loc[0,"rank of -4"]=c[7]
          for v in range(d) :
           e=[]
           f=[]
           g=[]
           for q in range(8) : 
            g.append(0)
           e.append(df["+1"][v+2])
           e.append(df["-1"][v+2])
           e.append(df["+2"][v+2])
           e.append(df["-2"][v+2])
           e.append(df["+3"][v+2])
           e.append(df["-3"][v+2])
           e.append(df["+4"][v+2])
           e.append(df["-4"][v+2])
           f.append(df["+1"][v+2])
           f.append(df["-1"][v+2])
           f.append(df["+2"][v+2])
           f.append(df["-2"][v+2])
           f.append(df["+3"][v+2])
           f.append(df["-3"][v+2])
           f.append(df["+4"][v+2])
           f.append(df["-4"][v+2])
           f.sort(reverse = True)
           for i in range(8) : 
                for j in range(8) : 
                    if e[j]==f[i] :
                        g[j]=i+1
                        j=9
           df.loc[v+2,"rank of +1"]=g[0]                 
           df.loc[v+2,"rank of -1"]=g[1]                 
           df.loc[v+2,"rank of +2"]=g[2]
           df.loc[v+2,"rank of -2"]=g[3]
           df.loc[v+2,"rank of +3"]=g[4]
           df.loc[v+2,"rank of -3"]=g[5]
           df.loc[v+2,"rank of +4"]=g[6]
           df.loc[v+2,"rank of -4"]=g[7]
           w=[]
           c=0
           w.append(df["rank of +1"][0])
           w.append(df["rank of -1"][0])
           w.append(df["rank of +2"][0])
           w.append(df["rank of -2"][0])
           w.append(df["rank of +3"][0])
           w.append(df["rank of -3"][0])
           w.append(df["rank of +4"][0])
           w.append(df["rank of -4"][0])
          
           for j in range(8) :
               if w[j]==1 :
                   c=j
                   if(c==0) :
                      c=1
                      df.loc[0,"Rank1 Octant ID"]=c
                      j=8
                   if(c==1) :
                      c=-1
                      df.loc[0,"Rank1 Octant ID"]=c
                      j=8
                   if(c==2) :
                      c=2
                      df.loc[0,"Rank1 Octant ID"]=c
                      j=8
                   if(c==3) :
                      c=-2
                      df.loc[0,"Rank1 Octant ID"]=c
                      j=8
                   if(c==4) :
                       c=3
                       df.loc[0,"Rank1 Octant ID"]=c
                       j=8
                   if(c==5) :
                       c=-3
                       df.loc[0,"Rank1 Octant ID"]=c
                       j=8
                   if(c==6) :
                       c=4
                       df.loc[0,"Rank1 Octant ID"]=c
                       j=8
                   if(c==7) :
                      c=-4
                      df.loc[0,"Rank1 Octant ID"]=c
                      j=8
           for i in range(d) :
              y=[]
              c=0
              y.append(df["rank of +1"][i+2])
              y.append(df["rank of -1"][i+2])
              y.append(df["rank of +2"][i+2])
              y.append(df["rank of -2"][i+2])
              y.append(df["rank of +3"][i+2])
              y.append(df["rank of -3"][i+2])
              y.append(df["rank of +4"][i+2])
              y.append(df["rank of -4"][i+2])
              for j in range(8) :
                  if y[j]==1 :
                      c=j
                      if(c==0) :
                         c=1
                         df.loc[i+2,"Rank1 Octant ID"]=c
                         j=8
                      if(c==1) :
                         c=-1
                         df.loc[i+2,"Rank1 Octant ID"]=c
                         j=8
                      if(c==2) :
                         c=2
                         df.loc[i+2,"Rank1 Octant ID"]=c
                         j=8
                      if(c==3) :
                         c=-2
                         df.loc[i+2,"Rank1 Octant ID"]=c
                         j=8
                      if(c==4) :
                          c=3
                          df.loc[i+2,"Rank1 Octant ID"]=c
                          j=8
                      if(c==5) :
                          c=-3
                          df.loc[i+2,"Rank1 Octant ID"]=c
                          j=8
                      if(c==6) :
                          c=4
                          df.loc[i+2,"Rank1 Octant ID"]=c
                          j=8
                      if(c==7) :
                         c=-4
                         df.loc[i+2,"Rank1 Octant ID"]=c
                         j=8
          
          df.loc[d+5,"+1"]="OCTANT ID"
          k=0
          o=0
          n=d+6
          for i in range(8) :
              if(i%2==0) :
                  k=k+1
                  df.loc[n,"+1"]=k
                  n=n+1
              else :
                  o=o-1
                  df.loc[n,"+1"]=o
                  n=n+1
                  
          octant_name_id_mapping = {"1": "Internal outward interaction", "-1": "External outward interaction", "2": "External Ejection",
                                        "-2": "Internal Ejection", "3": "External inward interaction", "-3": "Internal inward interaction", "4": "Internal sweep", "-4": "External sweep"}      
          df.loc[d+5,"-1"]="Octant Name "
          df.loc[d+5,"+3"]="Count of Rank 1 Mod Values"
          k=0
          o=0
          n=d+6
          for i in range(8) :
              if(i%2==0) :
                  k=k+1
                  df.loc[n,"-1"]=octant_name_id_mapping[str(k)]
                  n=n+1
              else :
                  o=o-1
                  df.loc[n,"-1"]=octant_name_id_mapping[str(o)]
                  n=n+1
          df.loc[0,"Rank1 Octant Name"]=octant_name_id_mapping[str(int(df.loc[0,"Rank1 Octant ID"]))]
          for i in range(d) :
              df.loc[i+2,"Rank1 Octant Name"]=octant_name_id_mapping[str(int(df.loc[i+2,"Rank1 Octant ID"]))]
          p=df['Rank1 Octant ID'].value_counts()
          h=[]
          for i in range(d) :
              h.append(int(df["Rank1 Octant ID"][i+2]))
          k=0
          for i in range(d) :
              if(h[i]==1)  :
                  k=k+1
          df.loc[d+6,"+3"]=k
          k=0
          for i in range(d) :
              if(h[i]==-1)  :
                  k=k+1
          df.loc[d+7,"+3"]=k
          k=0
          for i in range(d) :
              if(h[i]==2)  :
                  k=k+1
          df.loc[d+8,"+3"]=k
          k=0
          for i in range(d) :
              if(h[i]==-2)  :
                  k=k+1
          df.loc[d+9,"+3"]=k
          k=0
          for i in range(d) :
              if(h[i]==3)  :
                  k=k+1
          df.loc[d+10,"+3"]=k
          k=0
          for i in range(d) :
              if(h[i]==-3)  :
                  k=k+1
          df.loc[d+11,"+3"]=k
          k=0
          for i in range(d) :
              if(h[i]==4)  :
                  k=k+1
          df.loc[d+12,"+3"]=k
          k=0
          for i in range(d) :
              if(h[i]==-4)  :
                  k=k+1
          df.loc[d+13,"+3"]=k
        
          df.to_excel('octant_output_ranking_excel.xlsx')
        except:
             print("please enter mod value greater than 0")    
     except :
      print("the input file does not exists/or any error")    

###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000 
octant_range_names(mod)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
