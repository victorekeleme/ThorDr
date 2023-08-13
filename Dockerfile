FROM python:alpine3.18

RUN apk update && apk add --update npm
    
RUN npm install webtorrent-cli -g -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./ThorBot.py" ]