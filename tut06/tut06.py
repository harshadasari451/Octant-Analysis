import pandas as pd
import math
import re

df = pd.read_csv("input_attendance.csv")
register_df = pd.read_csv("input_registered_students.csv")
att_dates = ["28/07/2022",
            "1/08/2022","04/08/2022",
            "08/08/2022","11/08/2022",
            "18/08/2022",
            "22/08/2022","25/08/2022",
            "29/08/2022","01/09/2022",
            "05/09/2022","08/09/2022",
            "12/09/2022","15/09/2022",
            "19/09/2022","26/09/2022",
            "29/09/2022","03/10/2022",
            "06/10/2022","10/10/2022",
            "13/10/2022","17/10/2022",
            "20/10/2022","24/10/2022",
            "27/10/2022","31/10/2022",
            "03/11/2022","07/11/2022",
            "10/11/2022","14/11/2022",
            "17/11/2022"]

str_time = "14"

df[["date","time"]]=df.Timestamp.str.split(" ",expand=True,)
df.loc[((re.fullmatch(df.date,att_dates)) and (14<=int((df.time).split(":")[0])<15)),"attend"] = "T-attend"
df.loc[(14>int((df.time).split(":")[0]) or (int((df.time).split(":")[0])>15)),"attend"] = "F-attend"
print(df)