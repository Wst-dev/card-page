FROM python:3.7.2-alpine3.8
RUN apk update && apk upgrade && apk add bash && pip install --upgrade pip
ENV SERVER_ADDRESS=0.0.0.0:80
COPY . .
RUN pip install -r req.txt
EXPOSE 80:80/tcp
EXPOSE 80:80/udp
ENTRYPOINT python main.py
