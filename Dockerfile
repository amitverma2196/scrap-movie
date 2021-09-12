FROM python:3.9

WORKDIR /code

COPY requirements.txt .

COPY imdblist.py .

COPY imdblist2.py .

RUN pip install -r requirements.txt


CMD [ "python3", "imdblist.py" ]
