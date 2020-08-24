from flask import Flask, jsonify, request
import scrap_task

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return '<h1>Just INDEX</h1>'


@app.route('/promotions/furshet', methods=['GET'])
def get_discounts():
    discounts = scrap_task.get_json()
    return jsonify(discounts)


@app.route('/promotions/furshet/withDiscount', methods=['POST'])
def with_discount():
    result_json = []
    body_data = request.get_json()
    discount_more_than = body_data["discountMoreThan"]
    discounts = scrap_task.get_json()

    for item in discounts:
        percent_string = str(item['discount'])
        if percent_string != "None":
            percent_string = percent_string[1:-1]  # Format output of percents: -22% -> 22
            if int(percent_string) > int(discount_more_than):
                print(item)
                result_json.append(item)

    return jsonify(result_json)


def main():
    app.run()


if __name__ == '__main__':
    main()