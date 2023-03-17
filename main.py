# import gunicorn as gunicorn
import requests, urllib.parse, urllib.request, urllib.error, json
from flask import Flask, render_template, request, flash
import requests
price_less_than = 0
app = Flask(__name__)
app.secret_key = 'heyguysweneedtokeepthisthingsecretorwhateer,sobasicallyimjusttypingandwhatwasisayingyeayeayea'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/preferences-page.html')
def preferences():
    return render_template('preferences-page.html')


@app.route('/products.html', methods=['POST'])
def products():
    final_products = []
    preferences = request.form['makeup']
    budget = float(request.form['budget'])

    # Call the Makeup API
    url = "https://makeup-api.herokuapp.com/api/v1/products.json"

    # Define response with a default value of None
    response = None

    # Set up query parameters for the API call
    #for(every preference){
     #   call API(prefernce)
      #  add results to current list
    #}
   # for each_pref in preferences:
        #flash(each_pref)
    params = {"product_type": preferences, "price_less_than": budget}
    response = requests.get(url, params)
    if response.status_code == 200:
        returned_products = response.json()
    else:
        returned_products = []
    final_products += returned_products

    # Check if response is defined
    if response:

        # Parse the response and return the list of products
        #returned_products = response.json()

        # Filter products based on user preferences and budget

        # filtered_products = []
        # for product in returned_products:
        #     price = float(product['price']) if product['price'] else None
        #     matches_preferences = [preference in product['product_type'] for preference in preferences]
        #     meets_budget = price is not None and price <= budget
        #     if all(matches_preferences) and meets_budget:
        #         filtered_products.append(product)
        if len(final_products) > 0:
            return render_template('products.html', products=final_products)
        else:
            return render_template('no_products.html')

    # Handle case where response is not defined
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
