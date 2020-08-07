FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY ./requirements.txt ./

RUN apt-get update; apt-get install --reinstall -y curl vim
RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 8080
CMD [ "python", "main.py" ]
