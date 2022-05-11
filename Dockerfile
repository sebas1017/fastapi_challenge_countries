FROM python:3.8

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src


RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]