import time
import json
from bson.json_util import dumps
from datetime import datetime
from flask import Response


def current_epoch():
    """
    returns current time while updating measures or value-set.
    """
    cur_timestamp = datetime.now()
    return int(cur_timestamp.strftime("%s"))*1000 +\
                 int(cur_timestamp.microsecond/1000)


def send_response(data, status_code):
    if isinstance(data,str):
        return Response(
            response= str(data),
            status= int(status_code)
        )
	return Response(
	        response=json.dumps(data),
	        status= int(status_code)
	    )