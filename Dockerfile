FROM python:3.10

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

CMD [ "python", "main.py"]