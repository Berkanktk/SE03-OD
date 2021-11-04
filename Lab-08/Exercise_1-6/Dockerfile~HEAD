FROM ubuntu

RUN apt-get update && apt-get install build-essential -y

RUN apt-get install htop -y

COPY . .

RUN make all