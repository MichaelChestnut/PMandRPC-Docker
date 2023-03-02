# syntax=docker/dockerfile:1

FROM ubuntu:22.04

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

RUN apt-get update

RUN apt-get install -y python3 python3-pip

#RUN apt-get update && \
#      apt-get -y install sudo

#RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN pip3 install adafruit-circuitpython-ina219

RUN apt-get install -y python3-smbus python3-dev i2c-tools

RUN apt-get install -y python3-lgpio

RUN pip install rpi.gpio

RUN apt install -y software-properties-common

RUN apt-add-repository ppa:mosquitto-dev/mosquitto-ppa

RUN apt-get update

RUN apt-get install -y mosquitto mosquitto-clients

RUN service mosquitto start

COPY NewMosquitto.conf /etc/mosquitto/conf.d

RUN service mosquitto restart

RUN pip3 install paho-mqtt

RUN pip install pytz

ADD PMConfiguration.py /PMConfiguration.py

ADD PowerMonitor.py /PowerMonitor.py

RUN chmod +x /PowerMonitor.py 

CMD bash

#RUN python3 PowerMonitor.py

#done
