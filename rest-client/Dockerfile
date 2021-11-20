#Pull base image
FROM python

COPY . /
RUN pip install pipenv
RUN pipenv install --skip-lock

ENV FLASK_APP app.py
ENTRYPOINT ["pipenv", "run","flask","run","--host=0.0.0.0"]
