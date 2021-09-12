FROM python:3

WORKDIR /code

COPY requirements.txt .

COPY imdblist.py .

COPY imdblist2.py .

RUN pip3 install -r requirements.txt


CMD [ "python3", "imdblist.py" ]
