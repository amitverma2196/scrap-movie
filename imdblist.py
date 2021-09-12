from bs4 import BeautifulSoup
import requests
# import re
from sys import argv

if len(argv) < 2:
    print('Please pass the TOP value as filename.py TOP[0 - 10]')
    exit()

print('Top : ' + str(argv[1]))
top = int(argv[1])

print("Getting Top "+str(argv[1])+" movies detail from IMDB\n")

url = 'https://www.imdb.com/chart/boxoffice'
response = requests.get(url)
# print(response.text[:550])
soup = BeautifulSoup(response.text, 'html.parser')

# print(movies)

# movielist = soup.find_all('td',"titleColumn" , limit=2)
# print(movielist)

movies = soup.select('td.titleColumn')
# print(movies)
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
cast = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]

# create a empty list
list = []

# Iterating over movies to extract
# each movie's details
for index in range(0, top):
    title = movies[index].get_text().replace("\n",'')
    # star_cast =  crew[index],
    place = index+1
    data = { "sn": place,
             "title": title,
             "cast": cast[index],
             "link": links[index]
             }
    list.append(data)

# printing movie details with its rating.
# print(list)
for movie in list:
    print(str(movie['sn']) + ' - ' + movie['title']+ ' - '+ ' Cast: ' + movie['cast'])

