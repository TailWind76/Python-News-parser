import requests
from bs4 import BeautifulSoup

def get_news_data(url, tag_name):
    try:
        # Запрос к сайту
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешность запроса

        # Создание объекта BeautifulSoup для парсинга HTML-кода
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ищем все элементы с указанным тегом (например, <h2> или <h3>)
        elements = soup.find_all(tag_name)

        # Выводим информацию для каждого элемента
        for element in elements:
            print(element.text.strip())  # .strip() удаляет лишние пробелы и переносы строк

    except requests.exceptions.MissingSchema:
        print("Ошибка: Некорректный URL. Убедитесь, что вы ввели URL в правильном формате (например, https://example.com).")

    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка HTTP: {http_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"Ошибка запроса: {req_err}")

if __name__ == "__main__":
    url_to_parse = input("Введите URL сайта с новостями: ")
    tag_to_parse = input("Введите тег, содержащий заголовки новостей (например, h2, h3 и т.д.): ")
    get_news_data(url_to_parse, tag_to_parse)
