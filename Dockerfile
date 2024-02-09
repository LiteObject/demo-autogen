FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org pyautogen docker

CMD [ "python", "app.py" ]