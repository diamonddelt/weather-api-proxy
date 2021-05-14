FROM python:3

COPY ./app app

RUN pip3 install -r app/requirements.txt

CMD ["python", "./app/main.py"]