from flask import Blueprint, request
from flask_restful import Api, Resource


# api initialization
sensor_pb = Blueprint("SensorDataReader",__name__)
Sensor_Reader_API = Api(sensor_pb)

currentX = 0
currentY = 0

class SensorReader(Resource):

    def get(self):
        return {"x_value":currentX, "y_value":currentY}
    
    def post(self):
        global currentX
        global currentY

        if not 'x' in request.json:
            return {"error": "x-value shouldn't be none"}
        
        if not 'y' in request.json:
            return {"error": "y-value shouldn't be none"}
        
        x_value = request.json['x']
        y_value = request.json['y']

        # update current_x, current_y
        currentX = x_value
        currentY = y_value

        
class Test(Resource):
    def get(self):
        return "Sensor Server is working"
        
# routing
Sensor_Reader_API.add_resource(SensorReader, "/readings") 
Sensor_Reader_API.add_resource(Test, "/")
