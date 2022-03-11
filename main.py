from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timeanddate.com/weather/bulgaria/sofia')

soup = BeautifulSoup(html_text.text, 'lxml')
country = 'Sofia Bulgaria'
# Here is the forescast for today
forecast = soup.find('section', class_='bk-focus').span.text
feels_like = soup.find('section', class_='bk-focus').p.get_text()

print(f'The forecast for two weeks in {country}:')
for item in soup.find_all('td', class_='wa'):
      print(f'Forecast for {item.div.text} : {item.p.text}\n')

# print(f'{country} \n'
#       f'{feels_like}\n'
#       f'Todays {forecast}')