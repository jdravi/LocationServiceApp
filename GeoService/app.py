from flask import Flask
from flask_limiter import Limiter
from Model import LocalityManager
from flask import Flask, make_response
import json
from Util import json_response, JSON_MIME_TYPE
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["600 per hour"]
)


@app.route('/')
def start():
    return 'Welcome to Location Service App ' \
           + "\n" + '/user : for list of city as per user entered the keyword' \
                    "\n" + '/location : for list of locality based on user location and within given distance '


@app.route("/user")
@limiter.limit("100 per minute")
def suggest_locations():
    loc_mgr = LocalityManager.LocalityManager()

    """Prepare Input for Model API based on userInput """
    """ hard coded input params """
    user_lat = 13.225555555555555
    user_long = 77.575
    limit = 5
    user_key = "Delhi"
    data = loc_mgr.most_relevent_result_usr(user_lat, user_long, limit, user_key)
    if data is None or len(data) == 0:
        return json_response(json.dumps({"result : ": "No Result Found "}))
    return json_response(json.dumps(data))


@app.route("/location")
@limiter.limit("100 per minute")
def location_based_on_lat_long():
    loc_mgr = LocalityManager.LocalityManager()

    """Prepare Input for Model API based on userInput """

    user_lat = 13.225555555555555
    user_long = 77.575
    dist = 20
    data = loc_mgr.get_locality_within_dis(user_lat, user_long, dist)

    if data is None:
        return json_response("No Result Found ")
    return json_response(json.dumps(data))


def mandatory_parameter_check(params):

    """ to Check for mandatory Parameter in coming request  """
    required_params = ['user_text', 'latitude', 'longitude']
    result = {
        'fault ': False,
        'cause ': " "
    }

    cause = "Mandatory parameter missing : "
    for req_param in required_params:
        if req_param not in params:
            cause = cause + " " + req_param
            result['fault '] = True
            result['cause'] = cause

    return result


if __name__ == '__main__':
    app.run()
