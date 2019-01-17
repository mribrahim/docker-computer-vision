FROM python:3.6
MAINTAINER mribrahim

# Core linux dependencies.
RUN apt-get update

# Install system packages
RUN apt-get install -y \
build-essential \
cmake \
git \
wget \
unzip \
yasm \
pkg-config \
libswscale-dev \
libtbb2 \
libtbb-dev \
libjpeg-dev \
libpng-dev \
libtiff-dev \
libavformat-dev \
libpq-dev \
&& rm -rf /var/lib/apt/lists/*

# Install core packages 
RUN  pip install -U pip \
 numpy \
 opencv-python \
 scipy \ 
 scikit-image \
 scikit-learn \
 hdf5storage \
 h5py \
 matplotlib \
 pandas \
 tensorflow \
 keras \
 dlib


