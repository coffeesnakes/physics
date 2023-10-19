FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y hugo
COPY . /my_sre_school_web
WORKDIR /my_sre_school_web
CMD ["hugo", "server", "--bind", "0.0.0.0"]