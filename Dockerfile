FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python-mysqldb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000