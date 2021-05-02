from http import HTTPStatus
from flask import Flask

""" This is a simple server to serve the html page at the /static directory level."""

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def home_page():
    """ This function renders the index.html page.
        :returns html page
    """
    return app.send_static_file('index.html')

@app.route('/health/', methods=['GET'])
def health():
    """ This function renders the JSON message stating the health of the server.
        :returns JSON message and HTTP status code
    """
    return {'Status': 'Ok'}, HTTPStatus.OK



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
