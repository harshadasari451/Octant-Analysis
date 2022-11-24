
from datetime import datetime
start_time = datetime.now()

def attendance_report():
    df1 = pandas.read_csv(r"input_attendance.csv")
    df2 = pandas.read_csv(r"input_registered_students.csv")

    # dates of classes taken
    list1 = ["28-07-2022","01-08-2022","04-08-2022","08-08-2022","11-08-2022","15-08-2022","18-08-2022",
             "22-08-2022","25-08-2022","29-08-2022","01-09-2022","05-09-2022","08-09-2022","12-09-2022",
             "15-09-2022","19-09-2022","22-09-2022","26-09-2022","29-09-2022"]
    # holidays
    list2 = ["15-08-2022","18-08-2022"]
    # no class due to exams
    list3 = ["15-09-2022","19-09-2022","22-09-2022"]

    for i in range(0,len(df2["Roll No"])):
        cnt,cnt1,cnt2,cnt3,cnt5=0,0,0,0,0
        for j in range(0,len(df1["Attendance"])):
            if(df2.loc[i,"Roll No"] in df1.loc[j,"Attendance"]):
                cnt=cnt+1
        df = pandas.DataFrame()
        df.loc[0,"Date"] = " "
        df.loc[0,"Roll No"]=df2.loc[i,"Roll No"]
        df.loc[0,"Name"] = df2.loc[i,"Name"]
        df.loc[0,"Total Attendance Count"] = cnt
        ls=[]
        for j in range(0,len(df1["Timestamp"])):
            if(df2.loc[i,"Roll No"] in df1.loc[j,"Attendance"]):
               for  k,l in zip(list1,range(1,len(list1)+1)):
                    if(k in df1.loc[j,"Timestamp"] ):
                        if(k in ls):
                            cnt3=cnt3+1
                        else:
                         if(k not in list2 and k not in list3 and "14" in df1.loc[j,"Timestamp"] or "15.00" in df1.loc[j,"Timestamp"]):
                            cnt1=cnt1+1
                         elif(k not in list2 and k not in list3 and "14" not in df1.loc[j,"Timestamp"] and "15.00" not in df1.loc[j,"Timestamp"]):
                            cnt2=cnt2+1
                            cnt5=cnt5+1
                        ls.append(k)
                    elif(df1.loc[j,"Timestamp"][:10] not in list1):
                        cnt2=cnt2+1
                        break
        df.loc[0,"Real"] = cnt1
        df.loc[0,"Duplicate"] = cnt3
        df.loc[0,"Invalid"] = cnt2
        lst = []
        for j in range(0,len(df1["Timestamp"])):
            if(df2.loc[i,"Roll No"] in df1.loc[j,"Attendance"]):
               for  k,l in zip(list1,range(1,len(list1)+1)):
                    df.loc[l,"Date"]=k
                    if(k in df1.loc[j,"Timestamp"]):
                        if(k in lst):
                            df.loc[l,"Duplicate"]=1
                        else:
                         if(k not in list2 and k not in list3 and "14" in df1.loc[j,"Timestamp"] or "15.00" in df1.loc[j,"Timestamp"]):
                            df.loc[l,"Real"] = 1
                         elif(k not in list2 and k not in list3 and "14" not in df1.loc[j,"Timestamp"] and "15.00" not in df1.loc[j,"Timestamp"]):
                            df.loc[l,"Invalid"] = 1
                        lst.append(k)
        for j in range(0,len(df1["Timestamp"])):
            if(df2.loc[i,"Roll No"] in df1.loc[j,"Attendance"]):
               for  k,l in zip(list1,range(1,len(list1)+1)):
                  if(df1.loc[j,"Timestamp"][:10] not in list1):
                      df.loc[len(list1)+2,"Date"]=df1.loc[j,"Timestamp"][:10]
                      df.loc[len(list1)+2,"Invalid"]=1
                      break
        cnt4=0
        for j,k in zip(range(1,len(df["Date"])),list1):
            if(df.iloc[j,4]!=1 and k not in list2 and k not in list3):
                df.loc[j,"Absent"]=1
                cnt4=cnt4+1
        df.loc[0,"Absent"]=cnt4
        df.to_excel(r"output\{0}.xlsx".format(df2.loc[i,"Roll No"]), index=False)
    df3= pandas.DataFrame()
    for i in range(0,len(df2["Roll No"])):
        df3.loc[i,"Roll"]=df2.loc[i,"Roll No"]
        ct=0
        for  k in (list1):
           flag=0
           for j in range(0,len(df1["Timestamp"])):
            if(df2.loc[i,"Roll No"] in df1.loc[j,"Attendance"]):
                if(k in df1.loc[j,"Timestamp"] and k not in list2 and k not in list3 and "14" in df1.loc[j,"Timestamp"] or "15.00" in df1.loc[j,"Timestamp"] ):
                    df3.loc[i,k]="P"
                    ct=ct+1
                    flag=1
           if(flag==0 and k not in list2 and k not in list3):
                    df3.loc[i,k]="A"
        df3.loc[i,"Actual Lecture Taken"]=14
        df3.loc[i,"Total Real"]=ct
        df3.loc[i,"% Attendance"]=ct/14*100
    df3.to_excel(r"output\attendance_report_consolidated.xlsx", index=False)
import pandas
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
