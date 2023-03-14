# syntax=docker/dockerfile:1

FROM ubuntu:22.04

RUN apt-get update

RUN apt-get install -y python3 python3-pip

RUN apt-get install -y python3-smbus python3-dev i2c-tools

RUN apt install -y software-properties-common

RUN apt-add-repository ppa:mosquitto-dev/mosquitto-ppa

RUN apt-get update

RUN apt-get install -y mosquitto mosquitto-clients

COPY mosquitto.conf /etc/mosquitto/

RUN pip3 install paho-mqtt

RUN pip3 install rpi.gpio

RUN apt install -y python3-lgpio

RUN pip install pytz

RUN pip install pythonping

ADD RPCConfiguration.py /RPCConfiguration.py

ADD RemotePiControl.py /RemotePiControl.py
 
RUN chmod +x /RemotePiControl.py

CMD service mosquitto start \
    && python3 RemotePiControl.py \
    && bash

