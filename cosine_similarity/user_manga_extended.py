
import requests
import pandas as pd
import csv
import time
from urllib.error import HTTPError
import traceback



#response=requests.get('https://api.jikan.moe/v4/users/otaku86/mangalist')






#csv_writer.writerow(["Username","mal_id","score"])
 
#response=requests.get('https://api.jikan.moe/v4/Zurryyy/Bincal/mangalist')
#text=response.json()

# reading CSV file
data =pd.read_csv("output_users2.csv")



 
# converting column data to list
usernames = data['Username'].tolist()


attempts = 3

with open('users_manga2.csv','w')as new_file:
    csv_writer=csv.writer(new_file,delimiter=",")
    csv_writer.writerow(['Username','mal_id','score'])
    for user in usernames: 
        time.sleep(1)
        response=requests.get(f"https://api.jikan.moe/v4/users/{user}/mangalist")
        time.sleep(1)
        text=response.json()
        while attempts>0:
            try:
                for i in text['data']:
                    mal_id=i["manga"]["mal_id"] 
                    score=i["score"]
                    manga=[user,mal_id,score]
                    csv_writer.writerows([manga])
            except HTTPError:
                attempts -= 1
                time.sleep(1)
                continue
            except:
                print(traceback.format_exc())
            break
        #for i in text['data']:
          #  mal_id=i["manga"]["mal_id"] 
           # score=i["score"]
           # manga=[user,mal_id,score]
            #csv_writer.writerow([manga])
           # 
            #print(Username,mal_id,score)
