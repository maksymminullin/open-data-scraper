from pprint import pprint

import requests
from bs4 import BeautifulSoup


def main():

    url = "https://jobs.dou.ua/vacancies/?category=Node.js"

    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=custom_headers)

    result = BeautifulSoup(response.text, "html.parser")

    elements = result.select(".l-vacancy")

    vacancy_list = []

    for block in elements:
        element_data = block.select_one(".date")
        element_title = block.select_one(".vt")
        element_link = block.select_one(".vt")
        element_company_link = block.select_one(".company")
        element_location = block.select_one(".cities.bi.bi-geo-alt-fill")
        element_info = block.select_one(".sh-info")
        element_salary = block.select_one(".salary")

        item_vacancy = {
            "date": element_data.text.strip() if element_data else None,
            "vacancy_title": element_title.text.strip() if element_title else None,
            "vacancy_link": element_link["href"] if element_link else None,
            "company_name": element_company_link.text.strip()
            if element_company_link
            else None,
            "company_link": element_company_link["href"]
            if element_company_link
            else None,
            "location": element_location.text.strip() if element_location else None,
            "info": element_info.text.strip().replace("\xa0", " ")
            if element_info
            else None,
            "salary": element_salary.text.strip() if element_salary else None,
        }

        vacancy_list.append(item_vacancy)

    pprint(vacancy_list)


if __name__ == "__main__":
    main()
