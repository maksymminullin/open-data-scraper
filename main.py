from pprint import pprint
from typing import Any, Dict, Optional

import requests
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://jobs.dou.ua/vacancies/?category=Node.js"
CUSTOM_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}


def get_text_safe(element: Optional[Tag]) -> Optional[str]:
    if element:
        return element.text.strip().replace("\xa0", " ")
    return None


def get_attr_safe(element: Optional[Tag], attr: str) -> Optional[str]:
    if element and element.has_attr(attr):
        return element[attr]
    return None


def parse_vacancy_block(block: Tag) -> Dict[str, Any]:
    title_element = block.select_one(".vt")
    company_element = block.select_one(".company")

    return {
        "date": get_text_safe(block.select_one(".date")),
        "vacancy_title": get_text_safe(title_element),
        "vacancy_link": get_attr_safe(title_element, "href"),
        "company_name": get_text_safe(company_element),
        "company_link": get_attr_safe(company_element, "href"),
        "location": get_text_safe(block.select_one(".cities")),  # Спрощений селектор
        "info": get_text_safe(block.select_one(".sh-info")),
        "salary": get_text_safe(block.select_one(".salary")),
    }


def main():
    try:
        response = requests.get(BASE_URL, headers=CUSTOM_HEADERS)
        response.raise_for_status()  # Перевіряє, чи код відповіді 200 OK
    except requests.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.select(".l-vacancy")

    vacancy_list = [parse_vacancy_block(block) for block in elements]

    if len(vacancy_list) > 5:
        pprint(vacancy_list[5])
    else:
        print(f"Знайдено менше 6 вакансій. Всього знайдено: {len(vacancy_list)}")


if __name__ == "__main__":
    main()
