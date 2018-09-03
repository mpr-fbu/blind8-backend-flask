FROM python:3.6
MAINTAINER Raul Dagir <fburaul@gmail.com>
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python","index.py"]
