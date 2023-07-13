import pandas as pd
import requests
import json
import csv
import time
from urllib.error import HTTPError
import re
import traceback


df=pd.read_csv('mal_users_manga.csv')

id_values=df['manga_id'].unique()

id=id_values.tolist()
print(len(id))
print(id[-2])

new_id=id[3400:]

def genre_url_to_id(url):
    m = re.search('https://myanimelist.net/manga/genre/(\d+)/*', url)
    return m.group(0)


def get_genres(generss):
    genres=[]
    for g in generss:
        genre=g['name']
        genres.append(genre)
    return genres

def get_author(t):
    a=[]
    for authors in t:
        author=authors['name']
        a.append(author)
    return a

attempts = 3

"""""

with open('manga_df2.csv','w')as new_file:
    csv_writer=csv.writer(new_file,delimiter=",")
    csv_writer.writerow(['title','mal_id','type','chapters','volumes','status','genres','score','rank','author','serializations'])
    for manga in new_id: 
        response=requests.get(f"https://api.jikan.moe/v4/manga/{manga}")
        time.sleep(1)
        text=response.json()
        while attempts>0:
            try:
                for i in text:
                    title=text['data']['title']
                    mal_id=text['data']['mal_id']
                    type=text['data']['type']
                    chapters=text['data']['chapters']
                    volumes=text['data']['volumes']
                    status=text['data']['status']
                    score=text['data']['score']
                    rank=text['data']['rank']
                    author_unclean=text['data']['authors']
                    author=get_author(author_unclean)
                    serializations=text['data']['serializations'][0]['name']
                    geners_unclean=[{'id': genre_url_to_id(p['url']), 'name': p['name']} for p in text['data']['genres']]
                    genres=get_genres(geners_unclean)
                
                    manga=[title,mal_id,type,chapters,volumes,status,genres,score,rank,author,serializations]
                    
                    csv_writer.writerows([manga])
            except HTTPError:
                attempts -= 1
                time.sleep(1)
                continue
            except:
                print(traceback.format_exc())
            break
                


"""""