FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY accenture_test_model/ /code/accenture_test_model/
COPY routes/ /code/routes/
COPY validator/ /code/validator/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python app.py