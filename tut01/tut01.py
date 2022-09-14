#def octact_identification(mod=5000):
###Code


#from platform import python_version
#ver = python_version()

#if ver == "3.8.10":
#    print("Correct Version Installed")
#else:
#    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
#octact_identification(mod)

#print("hello")

import pandas as pd
df = pd.read_csv(r"octant_input.csv")  
# readed the input file and stored in dataframe called df

mod_i = mod
# stored the mod value in a temporary variable called mod_i
meanu = df['U'].mean()
# stored mean value of U in meanu
meanv = df['V'].mean()
# stored mean of V in meanv
meanw = df['W'].mean()
#stored mean of W in meanw

#pre-processing starts
# creating new empty coloumns called U avg, V avg, W avg
df['U Avg']= ''
df['V Avg']= ''
df['W Avg']= ''

# storing the values of meanu, meanv, meanw in 1st row of U avg,V avg,W avg
# by using .loc function
df.loc[0,['U Avg']] = meanu
df.loc[0,['V Avg']] = meanv
df.loc[0,['W Avg']] = meanw

#calculating u-u_avg and storing the value in df_u
#doing same for df_v and df_w
df['df_u'] = df['U']-meanu
df['df_v'] = df['V']-meanv
df['df_w'] = df['W']-meanw


#creating a coloumn called octant and using octant conditions to 
# give octant values to [u,v,w] system

#using .loc function to use octant conditions and storing the the 
#values in octant coloumns
df.loc[((df.df_u>0) & (df.df_v>0) & (df.df_w>0)),"octant"] = "+1"
df.loc[((df.df_u>0) & (df.df_v>0) & (df.df_w<0)),"octant"] = "-1"
df.loc[((df.df_u<0) & (df.df_v>0) & (df.df_w>0)),"octant"] = "+2"
df.loc[((df.df_u<0) & (df.df_v>0) & (df.df_w<0)),"octant"] = "-2"
df.loc[((df.df_u<0) & (df.df_v<0) & (df.df_w>0)),"octant"] = "+3"
df.loc[((df.df_u<0) & (df.df_v<0) & (df.df_w<0)),"octant"] = "-3"
df.loc[((df.df_u>0) & (df.df_v<0) & (df.df_w>0)),"octant"] = "+4"
df.loc[((df.df_u>0) & (df.df_v<0) & (df.df_w<0)),"octant"] = "-4"



o_1p=0
o_1n=0
o_2p=0
o_2n=0
o_3p=0
o_3n=0
o_4p=0
o_4n=0


for i in df['octant']:
    if i=="+1":
        o_1p = o_1p +1
    elif i == "-1":
        o_1n = o_1n + 1
    elif i == "+2":
        o_2p = o_2p + 1
    elif i == "-2":
        o_2n = o_2n + 1
    elif i == "+3":
        o_3p = o_3p + 1
    elif i == "-3":
        o_3n = o_3n + 1
    elif i == "+4":
        o_4p = o_4p + 1
    elif i == "-4":
        o_4n = o_4n + 1



df[''] = ''

df.loc[1,['']] = 'user input'


df['Octant ID']= ''
df['+1']= ''
df['-1']= ''
df['+2']= ''
df['-2']= ''
df['+3']= ''
df['-3']= ''
df['+4']= ''
df['-4']= ''

df.loc[1,['Octant ID']] = 'mod ' + str(mod_i)

df.loc[0,['Octant ID']] = ['Overall count']

df.loc[0,['+1']] = o_1p
df.loc[0,['-1']] = o_1n
df.loc[0,['+2']] = o_2p
df.loc[0,['-2']] = o_2n
df.loc[0,['+3']] = o_3p
df.loc[0,['-3']] = o_3n
df.loc[0,['+4']] = o_4p
df.loc[0,['-4']] = o_4n





len = len(df)
i = 1
start = 0
last = mod_i

while last<= len:
    df['Octant ID'][i+1] = str(start) + "-" + str(last-1)
    l_1p=0
    l_1n=0
    l_2p=0
    l_2n=0
    l_3p=0
    l_3n=0
    l_4p=0
    l_4n=0    
    for j in range(start,last):
        if df['octant'][j]=="+1":
            l_1p = l_1p +1
        elif df['octant'][j] == "-1":
            l_1n = l_1n + 1
        elif df['octant'][j] == "+2":
            l_2p = l_2p + 1
        elif df['octant'][j] == "-2":
            l_2n = l_2n + 1
        elif df['octant'][j] == "+3":
            l_3p = l_3p + 1
        elif df['octant'][j] == "-3":
            l_3n = l_3n + 1
        elif df['octant'][j] == "+4":
            l_4p = l_4p + 1
        elif df['octant'][j] == "-4":
            l_4n = l_4n + 1
    df.loc[i+1,['+1']] = l_1p
    df.loc[i+1,['-1']] = l_1n
    df.loc[i+1,['+2']] = l_2p
    df.loc[i+1,['-2']] = l_2n
    df.loc[i+1,['+3']] = l_3p
    df.loc[i+1,['-3']] = l_3n
    df.loc[i+1,['+4']] = l_4p
    df.loc[i+1,['-4']] = l_4n
    start = last
    i=i+1
    last = mod_i*i



if last>len:
    df['Octant ID'][i+1] = str(start) + "-" + str(len-1)
    p_1p=0
    p_1n=0
    p_2p=0
    p_2n=0
    p_3p=0
    p_3n=0
    p_4p=0
    p_4n=0
    for j in range(start,len):
        if df['octant'][j]=="+1":
            p_1p = p_1p +1
        elif df['octant'][j] == "-1":
            p_1n = p_1n + 1
        elif df['octant'][j] == "+2":
            p_2p = p_2p + 1
        elif df['octant'][j] == "-2":
            p_2n = p_2n + 1
        elif df['octant'][j] == "+3":
            p_3p = p_3p + 1
        elif df['octant'][j] == "-3":
            p_3n = p_3n + 1
        elif df['octant'][j] == "+4":
            p_4p = p_4p + 1
        elif df['octant'][j] == "-4":
            p_4n = p_4n + 1     
    df.loc[i+1,['+1']] = p_1p
    df.loc[i+1,['-1']] = p_1n
    df.loc[i+1,['+2']] = p_2p
    df.loc[i+1,['-2']] = p_2n
    df.loc[i+1,['+3']] = p_3p
    df.loc[i+1,['-3']] = p_3n
    df.loc[i+1,['+4']] = p_4p
    df.loc[i+1,['-4']] = p_4n   
     

df.to_csv("octant_ouput.csv")

     







