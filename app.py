from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    # import controllers
    from controllers.MarketController import MarketController

    # TODO this needs to get reorganized
    market_controller = MarketController()
    
    @app.route('/markets')
    @cross_origin()
    def market_data():
        # get the custom tickers from the request URL parameters
        tickers = request.args.getlist('tickers')

        # if tickers are not provided, use the default list
        if not tickers:
            print('No tickers specified. Using default...')
            tickers = ['^GSPC', '^GSPTSE', 'GC=F', 'CL=F', 'BTC-USD']

        # get the market data
        market_data = market_controller.get_market_data(tickers)

        return jsonify(market_data)

            
    @app.route('/markets/<ticker>')
    @cross_origin()
    def single_ticker_data(ticker):
        ticker_data = market_controller.get_single_ticker(ticker)
        return jsonify(ticker_data)
    
    @app.route('/dummy_markets')
    @cross_origin()
    def dummy_data():
        dummy_data = market_controller.get_dummy_data()
        return jsonify(dummy_data)

    # test route
    @app.route('/')
    def hello_world():
        return "Izzy is pretty"

    # error handler
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found"}), 404

    return app

app = create_app()
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run()