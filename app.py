import requests as requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    # print(data)
    # return str(source_currency) + " " + str(amount) + " " + str(target_currency)
    print(source_currency)
    print(amount)
    print(target_currency)


    cf = fetch_conversion_factor(source_currency, target_currency, amount)
    final_amount = cf * amount
    print(final_amount)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
    }
    return jsonify(response)
    # print(response)



def fetch_conversion_factor(source, target, amount):
    url = "https://api.fastforex.io/convert?from={}&to={}&" \
          "amount={}&api_key=735211a774-7a800ec8b4-rm3qwc".format(source, target,amount)

    response = requests.get(url)
    response = response.json()
    # print(response)
    result = response['result']['rate']
    # print(result)
    return result


if __name__ == "__main__":
    app.run(debug=True)

