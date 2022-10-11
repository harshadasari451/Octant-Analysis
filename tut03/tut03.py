from platform import python_version
from platform import mac_ver
from re import M
from sqlite3 import Row
import pandas as pd
from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0

def octant_longest_subsequence_count():
###Code
#excel_file = pd.ExcelFile('input_octant_transition_identify.xlsx')
    df = pd.read_excel('input_octant_longest_subsequence.xlsx')  
    # readed the input file and stored in dataframe called df

    
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

    ### preprocessing end here

    ##################################################################
    a=[]   #create an array a for counting sequence (+1 to -4)
    for i in range(9) :            
        a.append(0)    # insert all elements to 0 in an a[]array 
    b=[]   # create an array b for storing maximum length of each subsequence for (+1 to -4)
    for i in range(9) : 
        b.append(0)     # insert all elements to 0's in a b[]array
    c=[]    # create an array c to store the count of maximum length of each subsequence for (+1 to -4)
    for i in range(9) : 
        c.append(0)  # inserting all elements to 0's in a c[]array
    length=len(df)
    for i in range(length-1) :
        a[int(df["octant"][i])+4]=a[int(df["octant"][i])+4]+1 # increment the count of each part of subsequene
        if a[int(df["octant"][i])+4] != a[int(df["octant"][i+1])+4]:
            if(a[int(df["octant"][i])+4]>b[int(df["octant"][i])+4]):
                b[int(df["octant"][i])+4]=max(a[int(df["octant"][i])+4],b[int(df["octant"][i])+4])#find max length of each subsequence
                c[int(df["octant"][i])+4]=1 
                a[int(df["octant"][i])+4] =0
            else :
                if(a[int(df["octant"][i])+4]==b[int(df["octant"][i])+4]):
                    c[int(df["octant"][i])+4] += 1 # increment count for each subsequence of maximum length
                    a[int(df["octant"][i])+4] =0
                if (a[int(df["octant"][i])+4]<b[int(df["octant"][i])+4]):
                    a[int(df["octant"][i])+4] =0
    df.loc[0,""] = ""
    df.loc[0,"Count"] = "+1"
    df.loc[1,"Count"] = "-1"
    df.loc[2,"Count"] = "+2"
    df.loc[3,"Count"] = "-2"
    df.loc[4,"Count"] = "+3"
    df.loc[5,"Count"] = "-3"
    df.loc[6,"Count"] = "+4"
    df.loc[7,"Count"] = "-4"
    df.loc[0,"Longest Subsequence Length"] = b[5]           # storing maximum length of subsequence +1 in b[5]
    df.loc[1,"Longest Subsequence Length"] = b[3]           # storing maximum length of subsequence -1 in b[3]
    df.loc[2,"Longest Subsequence Length"] = b[6]           # storing maximum length of subsequence +2 in b[6]
    df.loc[3,"Longest Subsequence Length"] = b[2]           # storing maximum length of subsequence -2 in b[2]
    df.loc[4,"Longest Subsequence Length"] = b[7]           # storing maximum length of subsequence +3 in b[7]
    df.loc[5,"Longest Subsequence Length"] = b[1]           # storing maximum length of subsequence -3 in b[2]
    df.loc[6,"Longest Subsequence Length"] = b[8]           # storing maximum length of subsequence +4 in b[8]
    df.loc[7,"Longest Subsequence Length"] = b[0]           # storing maximum length of subsequence -4 in b[0]df.loc[0,"count"] = c[5]
    df.loc[0,"count"] = c[5]                                # storing count of maximum length of subsequence +1 in c[5]
    df.loc[1,"count"] = c[3]                                # storing count of maximum length of subsequence -1 in c[3]
    df.loc[2,"count"] = c[6]                                # storing count of maximum length of subsequence +2 in c[6]   
    df.loc[3,"count"] = c[2]                                # storing count of maximum length of subsequence -2 in c[2]     
    df.loc[4,"count"] = c[7]                                # storing count of maximum length of subsequence +3 in c[7]   
    df.loc[5,"count"] = c[1]                                # storing count of maximum length of subsequence -3 in c[1]   
    df.loc[6,"count"] = c[8]                                # storing count of maximum length of subsequence +4 in c[8]   
    df.loc[7,"count"] = c[0]                                # storing count of maximum length of subsequence -4 in c[0]   
    df.to_excel("output_octant_longest_subsequence.xlsx",index=False)



octant_longest_subsequence_count()



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))