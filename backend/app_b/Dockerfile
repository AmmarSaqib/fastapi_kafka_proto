FROM python:3.7

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"
