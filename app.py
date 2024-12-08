from flask import Flask, request, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Enable CORS globally
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Import controllers
    from controllers.MarketController import MarketController

    # Instantiate controller
    market_controller = MarketController()

    @app.route('/markets')
    def market_data():
        # Get the custom tickers from the request URL parameters
        tickers = request.args.getlist('tickers')

        # If tickers are not provided, use the default list
        if not tickers:
            print('No tickers specified. Using default...')
            tickers = ['^GSPC', '^GSPTSE', 'GC=F', 'CL=F', 'BTC-USD']

        # Get the market data
        market_data = market_controller.get_market_data(tickers)

        return jsonify(market_data)

    @app.route('/markets/<ticker>')
    def single_ticker_data(ticker):
        ticker_data = market_controller.get_single_ticker(ticker)
        return jsonify(ticker_data)

    @app.route('/dummy_markets')
    def dummy_data():
        dummy_data = market_controller.get_dummy_data()
        return jsonify(dummy_data)

    # Test route
    @app.route('/')
    def hello_world():
        return "Izzy is pretty"

    # Error handler
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found"}), 404

    return app

# Create the app
app = create_app()

if __name__ == '__main__':
    app.run()
