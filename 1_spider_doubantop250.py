import requests
from bs4 import BeautifulSoup
url = 'https://movie.douban.com/top250'
movies = []
pglist = ['0', '25', '50', '75', '100', '125', '150', '175', '200' ,'225', '250']

def parse_html(web_data):
	soup = BeautifulSoup(web_data,'html.parser')
	movie_list_soup = soup.find('ol', attrs = {'class':'grid_view'})
	for movie_li in movie_list_soup.find_all('li'):
		detail = movie_li.find('div', attrs = {'class':'hd'})
		movie_name = detail.find('span', attrs = {'class':'title'}).getText()
		movies.append(movie_name)

def main():
	with open('movies.txt','w') as ms:
		for i in pglist:
			payload = {'start':i}
			web_data = requests.get(url, params = payload).content
			parse_html(web_data)
		for j in movies:
			j=j+'\n'
			ms.write(j)

if __name__ == '__main__':
    main()





