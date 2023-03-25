from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

import network_glance.net_glance as net_g
import network_glance.device_glance as dev_g


import network_glance.endpoint_glance as end_g


app = Flask(__name__)
api = Api(app)

CORS(app)

class Net_Glance(Resource):

    def get(self):

        data = net_g.run()

        return {'data': data}, 200  # 200 OK code.

api.add_resource(Net_Glance, '/monitor/net_glance')


class Dev_Glance(Resource):

    def get(self):

        personal_devices = ["henry-armbian-rpi-4-model-b", "henry-windows-gaming-pc", "henry-ubuntu-surface-3"]
        data = dev_g.run(net_g.run(), personal_devices)

        return {'data': data}, 200  # 200 OK code.

api.add_resource(Dev_Glance, '/monitor/dev_glance')


class End_Glance(Resource):

    def get(self):

        data = end_g.run()

        return {'data': data}, 200  # 200 OK code.

api.add_resource(End_Glance, '/monitor/end_glance')





if __name__ == '__main__':
    app.run(host="0.0.0.0", port="4000")  # Runs the Flask app.
