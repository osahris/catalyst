FROM debian:bookworm

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-markdown \
    hugo \
    nodejs \
    npm \
    webpack \
    curl \
    jekyll \
    openjdk-17-jre \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g eslint-webpack-plugin fsh-sushi@3.3.3

RUN pip install -e .
