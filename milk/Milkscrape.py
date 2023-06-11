
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
import csv
# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_countries_by_milk_consumption_per_capita"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)

#scrape from
#https://medium.com/analytics-vidhya/web-scraping-a-wikipedia-table-into-a-dataframe-c52617e1f451

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'lxml')
indiatable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())


df.to_csv('data_scrape.csv')