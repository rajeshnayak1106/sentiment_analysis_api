<h1 align="center">Sentiment Analysis API</h1>

<!-- <p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/sentiment-analysis-api?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/sentiment-analysis-api?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/sentiment-analysis-api?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/sentiment-analysis-api?color=56BEB8"> -->

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/sentiment-analysis-api?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/sentiment-analysis-api?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/sentiment-analysis-api?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
  🚧  Sentiment Analysis Api 🚀 Under construction...  🚧
</h4>

<hr> -->

<!-- <p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#sparkles-features">Endpoints</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p> -->

<br>

## About

The Flask application provides two different endpoints for sentiment analysis of text data. One of that APIS takes a single sentence/paragraph and other one that takes a list of sentences/paragraphs. Based on assumptions line break/new line is takes as the list separator. The API uses a pre-trained sentiment analysis model to predict sentiment score. Based on the rules provided in the model classification document, if the prediction score is >= 0.0 then result is positive else negative. The API uses REST methodology and us written using Flask framework. There are many benefits of using REST format which benefits this API requirements such as

<br>
 * Ease of implementation : This API is very simple in nature  hence REST is best option 
<br>
* Supports JSON hence lightweight on network : There is no limitation in the lengths of text hence JSON would be the better format to transfer data over network as its semi-structured and also lightweight
 <br>
* Stateless : Each request to the endpoints need to be isolated from each other an the server side does not need to store the state of the request sent via the endpoints
 <br>

## API Documentation

There 2 API endpoints for multiple needs.
<br>
<b> /singleinput </b>
<br>
Accepts a single sentences/paragraph without line break and returns prediction score and sentiment analysis result in JSON format along with the text which was sent for analysis
<br>
<b> /listinput </b>
<br>
Accepts a list of sentences/paragraphs and returns prediction score and sentiment analysis result in JSON format for each sentences/paragraph in the list and also the overall list.

For better understanding please refer to the SwaggerHub link below

https://app.swaggerhub.com/apis/Personal8618/sentiment_analysis_api/1.0.0

## Technologies

The following technologies are used in this project:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Docker](https://www.docker.com/)

## Requirements

Before starting you need to have [Python](https://www.python.org/) installed.

## Running

```bash
# Clone this project
$ git clone https://github.com/rajeshnayak1106/sentiment_analysis_api

# Access
$ cd sentiment_analysis_api

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python app.py

# The server will initialize in the <http://localhost:5000>

# Test the endpoints
$ pytest api_test.py

# To run with docker
$ docker build -t sentiment_analysis_app:latest .
$ docker run -d -p 5000:5000 sentiment_analysis_api

```

<a href="#top">Back to top</a>
