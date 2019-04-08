from python:3.6-alpine

MAINTAINER stephen.knox@manchester.ac.uk

RUN apt-get update

RUN apt-get -y install locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

RUN apt-get install -y software-properties-common vim libmysqlclient-dev

COPY . /app
WORKDIR /app

CMD ["hydra-debug", "--help"]

ENTRYPOINT []
