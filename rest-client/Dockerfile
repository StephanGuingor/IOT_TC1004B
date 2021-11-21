#Pull base image
FROM python

WORKDIR /myapp
COPY . ./
RUN pip install pipenv
RUN pipenv install

ENV FLASK_APP app.py
ENTRYPOINT ["pipenv", "run","flask","run","--host=0.0.0.0"]
