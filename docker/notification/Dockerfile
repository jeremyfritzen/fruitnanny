FROM balenalib/raspberrypi3-debian-node:12.11-buster

RUN buildDeps="build-essential python-dev python3-dev python-setuptools python3-setuptools" \
    && echo 'APT::Install-Recommends "false";' >/etc/apt/apt.conf.d/00recommends \
    && echo 'APT::Install-Suggests "false";' >>/etc/apt/apt.conf.d/00recommends \
    && apt-get update \
    && apt-get install -y python-pip python3-pip \
    && apt-get install -y $buildDeps \
    && apt-get install -y libgpiod2 \
    && pip3 install adafruit-circuitpython-lis3dh \
    && pip3 install adafruit-circuitpython-dht \
    && pip3 install pushbullet.py \
    && apt-get --purge remove -y $buildDeps && apt-get --purge -y autoremove \
    && apt-get clean \
    && rm -rf /tmp/* \
    && rm -rf /var/lib/apt/lists/*

COPY ./docker/notification/temperature.py /
#CMD /bin/bash
CMD python3 /temperature.py