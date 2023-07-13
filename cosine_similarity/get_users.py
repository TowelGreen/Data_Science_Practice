import imp
from urllib import response
import csv
import requests
import json

#response=requests.get("https://api.jikan.moe/v4/anime/21/recommendations")
#response=requests.get("https://api.jikan.moe/v4/reviews/manga?&page=1")
#text=response.json()


#for i in text['data'] :
    #print(i['entry']['title'])
#print(text['data'][0]['entry']['title'])
with open('users.csv','w')as new_file:
    csv_writer=csv.writer(new_file,delimiter=",")
    csv_writer.writerow(['Username'])

    for p in range(15):
        response=requests.get(f"https://api.jikan.moe/v4/reviews/manga?&page={p}")
        text=response.json()
        for i in text['data']:
            print(i['user']['username']) 
            users=i['user']['username']
            csv_writer.writerows([users])