FROM ubuntu:18.04
MAINTAINER stephen.knox@manchester.ac.uk

RUN apt-get update

RUN apt-get -y install locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get install -y software-properties-common vim
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git libpq-dev libmysqlclient-dev

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

COPY . /app
WORKDIR /app

RUN chmod 755 install.sh
RUN ./install.sh

CMD ["hydra-debug", "--help"]
