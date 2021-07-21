# https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np

app = Flask(__name__)
api = Api(app)

with open('model_alcohol.pkl', 'rb') as f:
    model_alcohol = pickle.load(f)

with open('model_escape.pkl', 'rb') as f:
    model_escape = pickle.load(f)

with open('model_traffic.pkl', 'rb') as f:
    model_traffic = pickle.load(f)



# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('Category')
parser.add_argument('Type')
parser.add_argument('Year')
parser.add_argument('Month')

### Sample Input fields ###
# Category: 'Alkoholunfälle'
# Type: 'insgesamt,
# Year: '2021',
# Month: '01'


# @app.route("/", methods=['POST'])
class PredictSentiment(Resource):
    def post(self):
        # use parser and find the user's query
        args = parser.parse_args()
        category = args['Category']
        category_type = args['Type']
        year = int(args['Year'])
        month = int(args['Month'])

        if category == "Alkoholunfälle":
            prediction = model_alcohol.predict(n_periods=12)
            valid_flag = 0
        elif category == "Fluchtunfälle":
            # vectorize the user's query and make a prediction
            prediction = model_escape.predict(n_periods=12)
            valid_flag = 0
        elif category == "Verkehrsunfälle":
            # vectorize the user's query and make a prediction
            prediction = model_traffic.predict(n_periods=12)
            valid_flag = 0
        else:
            prediction = "Invalid Category. Choose from: Alkoholunfälle, Fluchtunfälle, Verkehrsunfälle "
            valid_flag = 1

        # create JSON object
        if valid_flag == 0: 
            output = {'prediction': prediction[month-1]}
        else:
            output = {'prediction' : prediction}
        # output = {'prediction': prediction[month-1]}
        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run()