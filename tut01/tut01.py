#def octact_identification(mod=5000):
###Code


#from platform import python_version
#ver = python_version()

#if ver == "3.8.10":
#    print("Correct Version Installed")
#else:
#    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

#mod=5000
#octact_identification(mod)

#print("hello")
import pandas as pd
df = pd.read_csv(r"octant_input.csv")
#print(df)

meanu = df['U'].mean()
meanv = df['V'].mean()
meanw = df['W'].mean()

'''
print(meanu)
print(meanv)
print(meanw)
'''

df['U Avg']= ''
df['V Avg']= ''
df['W Avg']= ''

df.loc[0,['U Avg']] = meanu
df.loc[0,['V Avg']] = meanv
df.loc[0,['W Avg']] = meanw


df['df_u'] = df['U']-meanu
df['df_v'] = df['V']-meanv
df['df_w'] = df['W']-meanw



#print(df)

df.loc[((df.df_u>0) & (df.df_v>0) & (df.df_w>0)),"Octant"] = "+1"
df.loc[((df.df_u>0) & (df.df_v>0) & (df.df_w<0)),"Octant"] = "-1"
df.loc[((df.df_u<0) & (df.df_v>0) & (df.df_w>0)),"Octant"] = "+2"
df.loc[((df.df_u<0) & (df.df_v>0) & (df.df_w<0)),"Octant"] = "-2"
df.loc[((df.df_u<0) & (df.df_v<0) & (df.df_w>0)),"Octant"] = "+3"
df.loc[((df.df_u<0) & (df.df_v<0) & (df.df_w<0)),"Octant"] = "-3"
df.loc[((df.df_u>0) & (df.df_v<0) & (df.df_w>0)),"Octant"] = "+4"
df.loc[((df.df_u>0) & (df.df_v<0) & (df.df_w<0)),"Octant"] = "-4"

#print(df)

o_1p=0
o_1n=0
o_2p=0
o_2n=0
o_3p=0
o_3n=0
o_4p=0
o_4n=0


for i in df['Octant']:
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
'''
print(o_1p)
print(o_1n)
print(o_2p)
print(o_2n)
print(o_3p)
print(o_3n)
print(o_4p)
print(o_4n)
'''

df['Octant ID']= ''
df['+1']= ''
df['-1']= ''
df['+2']= ''
df['-2']= ''
df['+3']= ''
df['-3']= ''
df['+4']= ''
df['-4']= ''

df.loc[0,['Octant ID']] = ['Overall count']

df.loc[0,['+1']] = o_1p
df.loc[0,['-1']] = o_1n
df.loc[0,['+2']] = o_2p
df.loc[0,['-2']] = o_2n
df.loc[0,['+3']] = o_3p
df.loc[0,['-3']] = o_3n
df.loc[0,['+4']] = o_4p
df.loc[0,['-4']] = o_4n



print(df)




