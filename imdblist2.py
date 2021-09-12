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
base_url = 'https://www.imdb.com'
response = requests.get(url)
# print(response.text[:550])
soup = BeautifulSoup(response.text, 'html.parser')

# print(movies)

movie_list = soup.find_all('td',"titleColumn" , limit=top)
# print(movielist)


# create a empty list
list = []

# Iterating over movies to extract
# each movie's details
index = 1
for movie in movie_list:

    # links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    # cast = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    title = movie.get_text().replace("\n",'')

    detail = movie.find("a")
    # print(detail['title'])
    # print(detail['href'])

    print("Getting Cast of movie " + str(title) + "  \n")

    movie_url = base_url+detail['href']+"/fullcredits"
    # print(movie_url)
    movie_response = requests.get(movie_url)
    # print(response.text[:550])
    soup = BeautifulSoup(movie_response.text, 'html.parser')
    # print(soup.prettify())
    cast_table = soup.find('table', { "class" : "cast_list"})
    # print(cast_table)
    trlist = cast_table.find_all("tr", limit=5)
    # print(trlist)
    i=1
    cast_list=[]
    for tr in trlist:
        if i ==1:
            i=1+1
            continue
        td = tr.select("td")
        cast_list.append(td[1].get_text().replace("\n",''))
        # print(td[1].get_text())
        # exit()
    # exit()
    # star_cast =  crew[index],
    # place = index
    cast_string = ", ".join(cast_list)
    data = { "sn": index,
             "title": title,
             "cast": detail['title'],
             "cast_list": cast_string,
             "link": detail['href']
             }
    list.append(data)
    index = index + 1

# printing movie details with its rating.
# print(list)
for movie in list:
    print(str(movie['sn'])+ ' - ' + movie['title']+ ' - ' + ' Cast: '+ movie['cast_list'])

