FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Update package lists
RUN apt-get update

# Install net-tools
RUN apt-get install -y net-tools
RUN apt-get install -y iputils-ping
RUN pip3 install quixstreams
RUN pip3 install quixstreams[postgresql]
# RUN pip3 install pymysql

