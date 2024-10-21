######## TASK1 ########

######## BUILD IMAGE ########
# docker build -f ./Dockerfile -t softy-pinko:task1 .

######## STARTUP CONTAINER ########
# docker run -p 5252:5252 -it --rm --name softy-pinko-task1 softy-pinko:task1

######## VERIFY ########
# http://127.0.0.1:5252/api/hello

FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED
RUN pip3 install flask
RUN pip3 install flask-cors

COPY ./api.py /app/api.py

WORKDIR /app
EXPOSE 5252

CMD ["python3", "api.py" ]
