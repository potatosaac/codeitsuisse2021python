import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stonks', methods=['POST'])
def evaluateprofit():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    print(data)
    logging.info("My result :{}".format(result))
    


