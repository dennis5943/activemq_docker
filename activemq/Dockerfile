FROM openjdk:11-jre

ADD . /app

WORKDIR /app

ENV ACTIVEMQ_TCP=61616 ACTIVEMQ_AMQP=5672 ACTIVEMQ_STOMP=61613 ACTIVEMQ_MQTT=1883 ACTIVEMQ_WS=61614 ACTIVEMQ_UI=8161
ENV ACTIVEMQ_HOME=/activemq

RUN apt-get update;apt-get install wget;apt-get install nano;
RUN tar zxvf apache-activemq-5.17.1-bin.tar.gz; mv ./apache-activemq-5.17.1 $ACTIVEMQ_HOME; 

COPY ./config/activemq.xml $ACTIVEMQ_HOME/conf
COPY ./config/jetty.xml $ACTIVEMQ_HOME/conf

WORKDIR $ACTIVEMQ_HOME

EXPOSE $ACTIVEMQ_TCP $ACTIVEMQ_AMQP $ACTIVEMQ_STOMP $ACTIVEMQ_MQTT $ACTIVEMQ_WS $ACTIVEMQ_UI

#CMD ["./bin/activemq",  "console","xbean:/app/config/activemq.xml"]
CMD ["./bin/activemq",  "console"]

#docker run --rm -v $PWD/config:/config -p 8161:8161 --rm  activemq ./bin/activemq console  xbean:/config/activemq.xml
#docker run --rm -v $PWD/config:/config -p 8161:8161 --rm  -it activemq bash
#docker run --rm -v $PWD/config:/config -p 8161:8161 --rm  -it activemq bash