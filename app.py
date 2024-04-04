from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from modelo.requerimientos_carros import EstandaresCarros

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins
logic = EstandaresCarros()

api = Api(
    app, 
    version='1.0', 
    title='Logic Prediccion Precios Carros',
    description='Logic Prediccion Precios Carros')

ns = api.namespace('logic')
   
parser = api.parser()

parser.add_argument(
'year', 
type=int, 
required=True, 
help='Car manufacture year', 
location='args')

parser.add_argument(
'mileage', 
type=int, 
required=True, 
help='Car mileage', 
location='args')

parser.add_argument(
'state', 
type=str, 
required=True, 
help='State where car is registered', 
location='args')

parser.add_argument(
'make',
type=str,
required=True,
help='Car make',
location='args')

parser.add_argument(
'model',
type=str,
required=True,
help='Car model',
location='args')

resource_fields = api.model('Resource', {
    'price': fields.Float
})

@ns.route('/predict_price')
class CarPricePrediction(Resource):
    
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        result = logic.predecir_precio(args['year'], args['mileage'], args['state'], args['make'], args['model'])    
        return {'result': result}, 200
        
if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0', port=5000)