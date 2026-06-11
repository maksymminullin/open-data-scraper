import requests
from bs4 import BeautifulSoup

custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

url = "https://jobs.dou.ua/vacancies/?category=Node.js"


def main():

    response = requests.get(url, headers=custom_headers)

    result = BeautifulSoup(response.text, "html.parser")

    result_vacancy = result.select(".l-vacancy")

    print(result_vacancy)


if __name__ == "__main__":
    main()
