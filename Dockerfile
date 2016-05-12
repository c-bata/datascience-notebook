From jupyter/datascience-notebook 
MAINTAINER Masashi Shibata <contact@c-bata.link>

USER root
RUN apt-get update && \
    apt-get install -y graphviz-dev graphviz && \
    rm -rf /var/lib/apt/lists/*

USER jovyan
RUN pip install pandas-validator outlier-utils

