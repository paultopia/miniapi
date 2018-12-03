#Grab the latest ubuntu image
FROM ubuntu:18.04

# to try and stop the texlive-xetex confirmation demands
# ENV DEBIAN_FRONTEND noninteractive
# seems to cause build to hand

# Install python and pip and pandoc
RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get install -y python3 python3-pip bash pandoc texlive
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# Run the image as a non-root user
RUN adduser --disabled-password --gecos '' myuser
# see: https://stackoverflow.com/questions/27701930/add-user-to-docker-container
USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT app:app 
# web: gunicorn app:app  ????
