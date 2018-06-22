import time
import json
from bson.json_util import dumps
from datetime import datetime
from flask import Response, jsonify

def current_epoch():
    """
    returns current time while updating measures or value-set.
    """
    cur_timestamp = datetime.now()
    return int(cur_timestamp.strftime("%s"))*1000 +\
                 int(cur_timestamp.microsecond/1000)


def send_response(res):
    data = {
        "status_code" : res[0],
        "data" : res[1] 
    }
    return Response(
        json.dumps(data),
        status = res[0]
    )