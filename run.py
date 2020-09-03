from flask import Flask
from flask import request
from geopy.geocoders import Nominatim

app = Flask(__name__)

geolocator = Nominatim(user_agent="geoapiExercises")


@app.route('/geo', methods=['GET'])
def address_to_geo():
    """Get request that returns coordinates from address"""

    address = request.args.get('address')
    try:
        coordinates = geolocator.geocode(address)
    except:
        return {'Error': 'Cannot find coordinates associated with given address'}

    payload = {
        'longitude': coordinates.longitude,
        'latitude': coordinates.latitude,
    }

    return payload


@app.route('/address', methods=['GET'])
def geo_to_address():
    """Get request that returns address from coordinates"""

    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    coordinates = "{},{}".format(latitude, longitude)

    try:
        address = geolocator.reverse(coordinates)
    except:
        return {'Error': 'Cannot find address for given coordinates'}

    payload = {
        'address': address.address,
    }

    return payload


if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True)

