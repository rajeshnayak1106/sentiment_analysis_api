
from flask import Flask, jsonify, request, json
from routes.request_handler import configure_routes


def test_post_single_recrod_route__success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000/sentimentanalysis/api/text/v1.0/singleinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = 'awesome motivational and inspiring'

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    assert response.status_code == 200


def test_post_list_records_route__success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000//sentimentanalysis/api/text/v1.0/listinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = 'awesome motivational and inspiring \n awesome motivational and inspiring'

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    assert response.status_code == 200


def test_post_single_record_route__response_structure():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000/sentimentanalysis/api/text/v1.0/singleinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = 'awesome motivational and inspiring'

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    dict_ = json.loads(response.data)
    assert 'score' in dict_ and 'error' not in dict_


def test_post_list_records_route__response_structure():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000//sentimentanalysis/api/text/v1.0/listinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = 'awesome motivational and inspiring'

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    dict_ = json.loads(response.data)
    assert 'results' in dict_ and 'error' not in dict_


def test_post_single_record_route__failure__bad_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000/sentimentanalysis/api/text/v1.0/singleinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = '11122132'

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    dict_ = json.loads(response.data)
    assert 'error' in dict_ and dict_[
        'message'] == 'Please provide valid text'


def test_post_single_record_route_blank_text__failure__bad_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000/sentimentanalysis/api/text/v1.0/singleinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = ' '

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    dict_ = json.loads(response.data)
    assert 'error' in dict_ and dict_[
        'message'] == 'Please provide valid text'


def test_post_list_route_blank_text__failure__bad_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000//sentimentanalysis/api/text/v1.0/listinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = ' '

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    dict_ = json.loads(response.data)
    assert 'error' in dict_ and dict_[
        'message'] == 'Please provide valid text'


def test_post_single_record_route_only_special_characters__failure__bad_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'http://localhost:5000/sentimentanalysis/api/text/v1.0/singleinput'

    mock_request_headers = {
        'Content-Type': 'text/plain'
    }

    mock_request_data = '!@#$%^&*()_+'

    response = client.post(url, data=mock_request_data,
                           headers=mock_request_headers)
    dict_ = json.loads(response.data)
    assert 'error' in dict_ and dict_[
        'message'] == 'Please provide valid text'
