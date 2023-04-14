import pandas as pd

data = {
 "period / day":{
    "0":'Monday',
    "1":'Tuesday',
    "2":'Wednesday',
    "3":'Thursday',
    "4":'Friday'
  },
 "year name with semester name":{
    "0":'2nd year  3rd semester',
    "1":'2nd year  3rd semester',
    "2":'2nd year  3rd semester',
    "3":'2nd year  3rd semester',
    "4":'2nd year  3rd semester'
 


 }
 }



df = pd.DataFrame(data)

print(df) 
