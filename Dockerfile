FROM openjdk:11

RUN apt-get update && \
    apt-get install -y unzip wget && \
    mkdir /ibkr && \
    cd /ibkr && \
    wget https://github.com/InteractiveBrokers/cpwebapi/releases/download/v1.0.0/CPWebAPI_Gateway_Installer_linux-x64.zip && \
    unzip CPWebAPI_Gateway_Installer_linux-x64.zip && \
    chmod +x ibgateway/ibgateway && \
    echo 'eula=true' > ibgateway/conf.yaml

WORKDIR /ibkr

EXPOSE 5000 8080

CMD ["java", "-jar", "ibgateway/ibgateway.jar"]
