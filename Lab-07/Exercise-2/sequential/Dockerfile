ROM ubuntu

COPY . ./

RUN apt-get update && apt-get install fio -y

CMD fio fio-seq-write.fio
