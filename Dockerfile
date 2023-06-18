FROM python:3.10-buster
WORKDIR /app
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./downloader.py .
ENTRYPOINT ["python","downloader.py"]

