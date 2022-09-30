'''
def octant_transition_count(mod=5000):
###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_transition_count(mod)
'''
#####  please igonre SettingWithCopy warning ######

mod=5000
#octact_identification(mod)

#print("hello")

from platform import mac_ver
from re import M
from sqlite3 import Row
import pandas as pd

#excel_file = pd.ExcelFile('input_octant_transition_identify.xlsx')
df = pd.read_excel('input_octant_transition_identify.xlsx')  
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
# nap using .loc function
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

#################################################################
#task-1 starts here

#created some variables to count octant values
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


#created empty coloumn
df[''] = ''
#named a 1st row in empty coloumn as 'user input' 
df.loc[1,['']] = 'user input'

#created the following coloumns
df['Octant ID']= ''
df['+1']= ''
df['-1']= ''
df['+2']= ''
df['-2']= ''
df['+3']= ''
df['-3']= ''
df['+4']= ''
df['-4']= ''

# inserted a name called mod 5000(for eg)
df.loc[1,['Octant ID']] = 'mod ' + str(mod_i)
#inserted a name called 'overall count'
df.loc[0,['Octant ID']] = ['Overall count']

#inserted the octant values in the dataframe
df.loc[0,['+1']] = o_1p
df.loc[0,['-1']] = o_1n
df.loc[0,['+2']] = o_2p
df.loc[0,['-2']] = o_2n
df.loc[0,['+3']] = o_3p
df.loc[0,['-3']] = o_3n
df.loc[0,['+4']] = o_4p
df.loc[0,['-4']] = o_4n


##############################################################

#Task-2 starts here

#created variable called len to store total no of rows 
len = len(df)

#loop to calculate octant values in mod ranges
i = 1
start = 0
last = mod_i

while last<= len:
    df['Octant ID'][i+1] = str(start) + "-" + str(last-1)
    # warning will be showed for name suggestions 
    #igonre the warning 'A value is trying to be set on a copy of a slice from a DataFrame'
    # and wait 
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
     
#created a octant_octput file using .to_csv function
#please delete  'octant_output.csv' file if it alredy exists in this directory


     

###################################################################################################
####### task-3 starts here ##############

### calculating overall transition count #####

df.loc[13,['']] = ['overall Transition Count']
df.loc[14,['+1']] = ['To']
df.loc[15,['Octant ID']] = ['count']
df.loc[16,['Octant ID']] = ['+1']
df.loc[17,['Octant ID']] = ['-1']
df.loc[18,['Octant ID']] = ['+2']
df.loc[19,['Octant ID']] = ['-2']
df.loc[20,['Octant ID']] = ['+3']
df.loc[21,['Octant ID']] = ['-3']
df.loc[22,['Octant ID']] = ['+4']
df.loc[23,['Octant ID']] = ['-4']
df.loc[15,['+1']] = ['+1']
df.loc[15,['-1']] = ['-1']
df.loc[15,['+2']] = ['+2']
df.loc[15,['-2']] = ['-2']
df.loc[15,['+3']] = ['+3']
df.loc[15,['-3']] = ['-3']
df.loc[15,['+4']] = ['-4']
df.loc[15,['-4']] = ['+4']

#### creating a 9 x 9 matrix to store the values of transition values
###  [adding 4 to each index +1,-1,+2,-2,+3,-3,+4,-4]

rows, cols = (9,9)
arr = [[0 for i in range(cols)] for j in range(rows)]
for pop in range(len-1) : 
    arr[int(df["octant"][pop])+4][int(df["octant"][pop+1])+4]=arr[int(df["octant"][pop])+4][int(df["octant"][pop+1])+4]+1
z=5    
for i in range(8) :
    if(i%2==0) :
      df["+1"][i+16]=arr[z][5]               # count of +1 - +1 is stored in arr[4+1][4+1]  
    if(i%2!=0) :                             # count of +1 - -1 is stored in arr[4+1][4-1]
       z=8-z                                 # count of +1 - +2 is stored in arr[4+1][2+4]
       df["+1"][i+16]=arr[z][5]              # count of +1 - -2 is stored in arr[1+4][-2+4]
       z=8-z                                 # count of +1 - +3 is stored in arr[4+1][3+4]
       z=z+1                                 # count of +1 - -3 is stored in arr[4+1][-3+4]
z=5                                          # count of +1 - +4 is stored in arr[4+1][4+4]
for i in range(8) :                          # count of +1 - -4 is stored in arr[4+1][-4+4]
    if(i%2==0) :
      df["-1"][i+16]=arr[z][3]
    if(i%2!=0) :                             # count of +2 - +1 is stored in arr[4+2][1+4]
       z=8-z                                 # count of +2 - -1 is stored in arr[4+2][-1+4]
       df["-1"][i+16]=arr[z][3]              # count of +2 - +2 is stored in arr[4+2][2+4]
       z=8-z                                 # count of +2 - -2 is stored in arr[4+2][-2+4]
       z=z+1                                 # count of +2 - +3 is stored in arr[4+2][3+4]
z=5                                          # count of +2 - -3 is stored in arr[4+2][-3+4]
for i in range(8) :                          # count of +2 - +4 is stored in arr[4+2][4+4]
    if(i%2==0) :                             # count of +2 - -4 is stored in arr[4+2][-4+4]
      df["+2"][i+16]=arr[z][6]
    if(i%2!=0) :
       z=8-z
       df["+2"][i+16]=arr[z][6]              # count of +3 - +1 is stored in arr[4+3][1+4]
       z=8-z                                 # count of +3 - -1 is stored in arr[4+3][-1+4]
       z=z+1                                 # count of +3 - +2  is stored in arr[4+3][2+4]
z=5                                          # count of +3 - -2  is stored in arr[4+3][-2+4]
for i in range(8) :                          # count of +3 - +3  is stored in arr[4+3][3+4]
    if(i%2==0) :                             # count of +3 - -3  is stored in arr[4+3][-3+4]
      df["-2"][i+16]=arr[z][2]               # count of +3 - +4  is stored in arr[4+3][4+4]
    if(i%2!=0) :                             # count of +3 - -4  is stored in arr[4+3][-4+4]
       z=8-z
       df["-2"][i+16]=arr[z][2]
       z=8-z
       z=z+1

z=5                                          # count of +4 - +1  is stored in arr[4+4][1+4]
for i in range(8) :                          # count of +4 - -1  is stored in arr[4+4][-1+4]
    if(i%2==0) :                             # count of +4 - +2  is stored in arr[4+4][2+4]
      df["+3"][i+16]=arr[z][7]               # count of +4 - -2  is stored in arr[4+4][-2+4]
    if(i%2!=0) :                             # count of +4 - +3  is stored in arr[4+4][3+4]
       z=8-z                                 # count of +4 - -3  is stored in arr[4+4][-3+4]
       df["+3"][i+16]=arr[z][7]              # count of +4 - +4  is stored in arr[4+4][4+4]
       z=8-z                                 # count of +4 - -4  is stored in arr[4+4][-4+4]
       z=z+1

z=5
for i in range(8) :
    if(i%2==0) :
      df["-3"][i+16]=arr[z][1]
    if(i%2!=0) :
       z=8-z
       df["-3"][i+16]=arr[z][1]
       z=8-z
       z=z+1
z=5
for i in range(8) :
    if(i%2==0) :
      df["+4"][i+16]=arr[z][8]
    if(i%2!=0) :
       z=8-z
       df["+4"][i+16]=arr[z][8]
       z=8-z
       z=z+1
z=5
for i in range(8) :
    if(i%2==0) :
      df["-4"][i+16]=arr[z][0]
    if(i%2!=0) :
       z=8-z
       df["-4"][i+16]=arr[z][0]
       z=8-z
       z=z+1


### creating a function to insert 9 x 9 matrix into data frame
# and to that using iterative method
 
def trans(first,end,mac):
    rows, cols = (9,9)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for pop in range(first,end-1) : 
        arr[int(df["octant"][pop])+4][int(df["octant"][pop+1])+4]=arr[int(df["octant"][pop])+4][int(df["octant"][pop+1])+4]+1
    z=5    
    for i in range(8) :
        if(i%2==0) :
            df['+1'][i+mac]=arr[z][5]            # count of +1 - +1 is stored in arr[4+1][4+1]   [adding 4 to each index +1,-1,+2,-2,+3,-3,+4,-4]
        if(i%2!=0) :                             # count of +1 - -1 is stored in arr[4+1][4-1]
            z=8-z                                # count of +1 - +2 is stored in arr[4+1][2+4]
            df['+1'][i+mac]=arr[z][5]            # count of +1 - -2 is stored in arr[1+4][-2+4]
            z=8-z                                # count of +1 - +3 is stored in arr[4+1][3+4]
            z=z+1                                # count of +1 - -3 is stored in arr[4+1][-3+4]
    z=5                                          # count of +1 - +4 is stored in arr[4+1][4+4]
    for i in range(8) :                          # count of +1 - -4 is stored in arr[4+1][-4+4]
        if(i%2==0) :
            df['-1'][i+mac]=arr[z][3]
        if(i%2!=0) :                             # count of +2 - +1 is stored in arr[4+2][1+4]
            z=8-z                                # count of +2 - -1 is stored in arr[4+2][-1+4]
            df["-1"][i+mac]=arr[z][3]            # count of +2 - +2 is stored in arr[4+2][2+4]
            z=8-z                                # count of +2 - -2 is stored in arr[4+2][-2+4]
            z=z+1                                # count of +2 - +3 is stored in arr[4+2][3+4]
    z=5                                          # count of +2 - -3 is stored in arr[4+2][-3+4]
    for i in range(8) :                          # count of +2 - +4 is stored in arr[4+2][4+4]
        if(i%2==0) :                             # count of +2 - -4 is stored in arr[4+2][-4+4]
            df["+2"][i+mac]=arr[z][6]
        if(i%2!=0) :
            z=8-z
            df["+2"][i+mac]=arr[z][6]            # count of +3 - +1 is stored in arr[4+3][1+4]
            z=8-z                                # count of +3 - -1 is stored in arr[4+3][-1+4]
            z=z+1                                # count of +3 - +2  is stored in arr[4+3][2+4]
    z=5                                          # count of +3 - -2  is stored in arr[4+3][-2+4]
    for i in range(8) :                          # count of +3 - +3  is stored in arr[4+3][3+4]
        if(i%2==0) :                             # count of +3 - -3  is stored in arr[4+3][-3+4]
            df["-2"][i+mac]=arr[z][2]            # count of +3 - +4  is stored in arr[4+3][4+4]
        if(i%2!=0) :                             # count of +3 - -4  is stored in arr[4+3][-4+4]
            z=8-z
            df["-2"][i+mac]=arr[z][2]
            z=8-z
            z=z+1

    z=5                                          # count of +4 - +1  is stored in arr[4+4][1+4]
    for i in range(8) :                          # count of +4 - -1  is stored in arr[4+4][-1+4]
        if(i%2==0) :                             # count of +4 - +2  is stored in arr[4+4][2+4]
            df["+3"][i+mac]=arr[z][7]            # count of +4 - -2  is stored in arr[4+4][-2+4]
        if(i%2!=0) :                             # count of +4 - +3  is stored in arr[4+4][3+4]
            z=8-z                                # count of +4 - -3  is stored in arr[4+4][-3+4]
            df["+3"][i+mac]=arr[z][7]            # count of +4 - +4  is stored in arr[4+4][4+4]
            z=8-z                                # count of +4 - -4  is stored in arr[4+4][-4+4]
            z=z+1

    z=5
    for i in range(8) :
        if(i%2==0) :
            df["-3"][i+mac]=arr[z][1]
        if(i%2!=0) :
            z=8-z
            df["-3"][i+mac]=arr[z][1]
            z=8-z
            z=z+1
    z=5
    for i in range(8) :
        if(i%2==0) :
            df["+4"][i+mac]=arr[z][8]
        if(i%2!=0) :
            z=8-z
            df["+4"][i+mac]=arr[z][8]
            z=8-z
            z=z+1
    z=5
    for i in range(8) :
        if(i%2==0) :
            df["-4"][i+mac]=arr[z][0]
        if(i%2!=0) :
            z=8-z
            df["-4"][i+mac]=arr[z][0]
            z=8-z
            z=z+1

    

mac = 27
i=1
start = 0
last = mod_i

while last<= len:

    ### making mod trasition table using while loop as did before
    df.loc[mac,['']] = ['mod Transition Count']
    df.loc[mac+1,['Octant ID']] = str(start)+'-'+str(last-1)
    df.loc[mac+1,['+1']] = ['To']
    df.loc[mac+2,['Octant ID']] = ['count']
    df.loc[mac+3,['Octant ID']] = ['+1']
    df.loc[mac+4,['Octant ID']] = ['-1']
    df.loc[mac+5,['Octant ID']] = ['+2']
    df.loc[mac+6,['Octant ID']] = ['-2']
    df.loc[mac+7,['Octant ID']] = ['+3']
    df.loc[mac+8,['Octant ID']] = ['-3']
    df.loc[mac+9,['Octant ID']] = ['+4']
    df.loc[mac+10,['Octant ID']] = ['-4']
    df.loc[mac+2,['+1']] = ['+1']
    df.loc[mac+2,['-1']] = ['-1']
    df.loc[mac+2,['+2']] = ['+2']
    df.loc[mac+2,['-2']] = ['-2']
    df.loc[mac+2,['+3']] = ['+3']
    df.loc[mac+2,['-3']] = ['-3']
    df.loc[mac+2,['+4']] = ['-4']
    df.loc[mac+2,['-4']] = ['+4']  
    trans(start,last,mac+3)



    mac = mac + 13
    start = last
    i=i+1
    last = mod_i*i

if last>len:
    df.loc[mac,['']] = ['mod Transition Count']
    df.loc[mac+1,['Octant ID']] = str(start)+'-'+str(len-1)
    df.loc[mac+1,['+1']] = ['To']
    df.loc[mac+2,['Octant ID']] = ['count']
    df.loc[mac+3,['Octant ID']] = ['+1']
    df.loc[mac+4,['Octant ID']] = ['-1']
    df.loc[mac+5,['Octant ID']] = ['+2']
    df.loc[mac+6,['Octant ID']] = ['-2']
    df.loc[mac+7,['Octant ID']] = ['+3']
    df.loc[mac+8,['Octant ID']] = ['-3']
    df.loc[mac+9,['Octant ID']] = ['+4']
    df.loc[mac+10,['Octant ID']] = ['-4']
    df.loc[mac+2,['+1']] = ['+1']
    df.loc[mac+2,['-1']] = ['-1']
    df.loc[mac+2,['+2']] = ['+2']
    df.loc[mac+2,['-2']] = ['-2']
    df.loc[mac+2,['+3']] = ['+3']
    df.loc[mac+2,['-3']] = ['-3']
    df.loc[mac+2,['+4']] = ['-4']
    df.loc[mac+2,['-4']] = ['+4']
    ## using trans function to count trasition count and insrt values into dataframe
    ##  please ignore warning "setting with copy "
    trans(start,len,mac+3)

df.to_excel("output_octant_transition_identify.xlsx")
