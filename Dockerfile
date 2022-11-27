# reference: https://hub.docker.com/_/ubuntu/
FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

# upgrade pip
RUN pip3 install --upgrade pip

# install python specific packages
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

# Rudimentary CLI Start
# docker run -it --rm -v $(pwd):/tf/notebooks -p 8888:8888 lyricgen
