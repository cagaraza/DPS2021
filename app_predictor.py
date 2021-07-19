# https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np

app = Flask(__name__)
api = Api(app)

model_path = 'model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)


# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('Category')
parser.add_argument('Type')
parser.add_argument('Year')
parser.add_argument('Month')


# Category: 'Alkoholunfälle'
# Type: 'insgesamt,
# Year: '2021',
# Month: '01'

class PredictSentiment(Resource):
    def post(self):
        # use parser and find the user's query
        args = parser.parse_args()
        category = args['Category']
        category_type = args['Type']
        year = int(args['Year'])
        month = int(args['Month'])
        # vectorize the user's query and make a prediction
        prediction = model.predict(n_periods=12)

        # create JSON object
        output = {'prediction': prediction[month-1],'category': category, 'type': category_type,'year': year,'month': month}
        
        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run()