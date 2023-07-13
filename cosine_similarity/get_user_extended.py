import imp
from urllib import response
import csv
import requests
import json



with open('users_part2.csv','w')as new_file:
    csv_writer=csv.writer(new_file,delimiter=",")
    csv_writer.writerow(['Username'])

    for p in range(8):
        response=requests.get(f"https://api.jikan.moe/v4/reviews/manga?&page={p}")
        text=response.json()
        for i in text['data']:
            print(i['user']['username']) 
            users=i['user']['username']
            csv_writer.writerows([users])