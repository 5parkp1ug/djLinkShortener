FROM python:3.7.8-slim

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
VOLUME /home/user/app/backend
WORKDIR /home/user/app/backend

# Install system dependencies
RUN apt update && apt install -y software-properties-common
RUN add-apt-repository ppa:ubuntugis/ppa
RUN apt install gcc build-essential binutils libproj-dev gdal-bin python3-gdal libgdal-dev -y

## Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

EXPOSE 8000
# Install app dependencies
COPY requirements.txt /home/user/app/backend
RUN pip install -r requirements.txt

USER user
