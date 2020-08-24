from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    result_json = []
    url = "https://furshet.ua/actions"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    html_soup = BeautifulSoup(html, 'html.parser')
    item_containers = html_soup.find_all('div', class_='item')

    for item in item_containers:
        product_name = item.find('div', class_='desc').text

        prices = item.find('div', class_='actions-list__price')
        old_price = prices.find('div', class_='old-cost')
        if old_price is not None:
            old_price = old_price.find('div', class_='del-cost').text
            old_price = str(int(old_price)/100)  # Format price output

        new_price = prices.find('div', class_='cost').text
        new_price = str(int(new_price)/100)  # Format price output

        discount = item.find('div', class_='sale')
        if discount is not None:
            discount = discount.text

        result_json.append(
            {
                "productName": product_name,
                "oldPrice": old_price,
                "newPrice": new_price,
                "discount": discount

            },
        )

    with open('output.json', 'w') as output_json:
        output_json.write(str(result_json))

if __name__ == '__main__':
    main()
