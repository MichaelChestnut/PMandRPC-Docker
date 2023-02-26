# syntax=docker/dockerfile:1

FROM ubuntu:22.04

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

RUN apt-get update

RUN apt-get install -y python3 python3-pip

RUN apt-get update && \
      apt-get -y install sudo

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN apt install -y software-properties-common

RUN apt-add-repository ppa:mosquitto-dev/mosquitto-ppa

RUN apt-get update

RUN apt-get install -y mosquitto mosquitto-clients

RUN service mosquitto start

ADD NewMosquitto.conf /NewMosquitto.conf

RUN cp NewMosquitto.conf /etc/mosquitto/conf.d

RUN service mosquitto restart

RUN pip3 install paho-mqtt

RUN pip3 install rpi.gpio

RUN apt install -y python3-lgpio

RUN pip install pytz

RUN pip install pythonping

#RUN git clone https://github.com/NAU-IoT/RemotePiReset.git

#RUN cd RemotePiReset

ADD RPRConfiguration.py /RPRConfiguration.py

ADD RemotePiReset.py /RemotePiReset.py
 
RUN chmod +x /RemotePiReset.py

#RUN python3 RemotePiReset.py

#done

