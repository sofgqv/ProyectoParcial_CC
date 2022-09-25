FROM python:3-slim
WORKDIR /proyectoparcial/api-admin
RUN pip3 install flask
RUN pip3 install flask-mysql
RUN pip3 install Flask-RESTful
RUN pip3 install pyjwt
COPY . .
CMD [ "python3", "./app.py" ]