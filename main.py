from bs4 import BeautifulSoup
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/result", methods=['GET'])
def result():
    html_text = requests.get('https://www.timeanddate.com/weather/bulgaria/sofia')

    soup = BeautifulSoup(html_text.text, 'lxml')
    country = 'Sofia Bulgaria'

    forecast = soup.find('section', class_='bk-focus').span.text
    feels_like = soup.find('section', class_='bk-focus').p.get_text()

    # this will be for two weeks
    # print(f'The forecast for two weeks in {country}:')
    # for item in soup.find_all('td', class_='wa'):
    #     print(f'Forecast for {item.div.text} : {item.p.text}\n')

    answer = (f'{country} \n'
          f'Todays {forecast}\n'
          f'{feels_like}')

    return answer


if __name__ == '__main__':
    app.run(debug=True)