from tensorflow.keras.models import load_model
import numpy as np
from flask import request, jsonify, Response
from validator.validations import check_for_multine, validate_text
import json


def configure_routes(app):

    # load the model and get a refrence
    model = load_model('accenture_test_model')

    # fucntuon to get the prediction score
    def get_prediction_score(text_list):

        prediction_score = model.predict(np.array(text_list))

        return prediction_score[0][0]

    # function to get the result based on prediction score
    def get_sentiment_analysis(score):

        return 'Positive' if score >= 0.0 else 'Negative'

    # api endpoint configuration to handle single sentence/paragrap
    @app.route('/sentimentanalysis/api/text/v1.0/singleinput', methods=['POST'])
    def single_line_endpoint():

        response_object = None
        response_code = None

        # capture data from the POST request
        text = request.data.decode('UTF-8')

        # validate input is not a list
        if check_for_multine(text):

            response_object = jsonify(
                {
                    'input': text,
                    'prediction score': None,
                    'result': '',
                    'error': 'invalid input',
                    'message': 'This endpoint only accepts a single senctence or a paragraph without line break'
                }
            )
            response_code = 400

        else:

            # check if the text input is valid input
            if validate_text(text):

                # get the prediction score
                score = get_prediction_score([text])

                # get the reuslt based on prediction score
                result = get_sentiment_analysis(score)

                response_object = jsonify(
                    {
                        'input': text,
                        'score': str(score),
                        'result': result
                    }
                )
                response_code = 200

            else:
                response_object = jsonify(
                    {
                        'input': text,
                        'score': None,
                        'result': '',
                        'error': 'invalid input',
                        'message': 'Please provide valid text'
                    }
                )
                response_code = 400

        return response_object, response_code

        # api endpoint configuration to handle list input

    @app.route('/sentimentanalysis/api/text/v1.0/listinput', methods=['POST'])
    def list_line_endpoint():

        response_object = None
        response_code = None
        valid_text_list = []
        overall_score = None
        overall_result = ''
        response_object_list = []
        response_object_list_item = None

        # capture data from the POST request
        texts = request.data.decode('UTF-8')

        # check if valid input provided
        if validate_text(texts):

            for text in texts.splitlines():

                if validate_text(text):

                    # get the prediction score
                    score = get_prediction_score([text])

                    # get the reuslt based on prediction score
                    result = get_sentiment_analysis(score)

                    response_object_list_item = {
                        'input': text,
                        'score': str(score),
                        'result': result
                    }

                    response_object_list.append(response_object_list_item)

                    valid_text_list.append(text)

            # combines the valid text in different lines
            combined_valid_text = ' '.join(
                [str(text) for text in valid_text_list])

            # get the prediction for combined text
            overall_score = get_prediction_score([combined_valid_text])

            # get result for combines text
            overall_result = get_sentiment_analysis(overall_score)

            # build the json structure for combined response
            response_object_list_item = {
                'combined_text': combined_valid_text,
                'combined_score': str(overall_score),
                'combined_result': overall_result,
            }

            response_object_list.append(response_object_list_item)

            response_object = json.dumps({'results': response_object_list})
            response_code = 200

        else:
            response_object = json.dumps(
                {
                    'input': texts,
                    'score': None,
                    'result': '',
                    'error': 'invalid input',
                    'message': 'Please provide valid text'
                }
            )
            response_code = 400

        return Response(response_object, response_code, mimetype='application/json')
