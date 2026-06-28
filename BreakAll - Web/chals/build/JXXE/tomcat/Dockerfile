#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

FROM openjdk:8u111-alpine

RUN apk add --update curl bash

# Add flag
RUN apk add coreutils
RUN apk add gcc
RUN apk add musl-dev
ADD flag /flag
RUN chmod 400 /flag
ADD readflag.c /readflag.c
RUN gcc /readflag.c -o /readflag
#RUN chmod +x /readflag
RUN chmod +s /readflag


ENV TOMCAT_VERSION 8.5.70
ADD apache-tomcat-$TOMCAT_VERSION.tar.gz /usr/local/
RUN mv /usr/local/apache-tomcat-$TOMCAT_VERSION /usr/local/tomcat
ENV CATALINA_HOME /usr/local/tomcat
WORKDIR /usr/local/tomcat


# Add a tomcat user
RUN addgroup -S tomcat && adduser -G tomcat -h /usr/local/tomcat -s /bin/bash -D tomcat
RUN chown -R tomcat:tomcat $CATALINA_HOME
RUN ls -lah $CATALINA_HOME

ENV RUN_USER tomcat
ENV RUN_GROUP tomcat
USER tomcat

EXPOSE 8080
CMD ["bin/catalina.sh","run"]
