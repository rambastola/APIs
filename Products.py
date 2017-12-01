import requests, json

def search_walmart(answer):
    """
    ask user for product's name then search for it in walmart.com.
    :param answer: information pulled from walmart.com
    :return: name of the product and price
    """
    encrypted = answer.content
    data = json.loads(encrypted)
    products = data["items"]

    for product in products:
        name = product["name"]
        price  = product["salePrice"]
        upc = product["upc"]
        #image = product["mediumImage"]
        rating = product["customerRating"]
        print(name, price, upc, rating)

def main():

    user = input("Enter product name ")
    response = requests.get("http://api.walmartlabs.com/v1/search?apiKey=bvngau7xave9du9m5wzhfdtb&query="+ user)
    search_walmart(response)

main()
