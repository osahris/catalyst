FROM debian:bookworm

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-markdown \
    && rm -rf /var/lib/apt/lists/*
