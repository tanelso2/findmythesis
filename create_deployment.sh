#!/bin/bash

zip -v deployment.zip \
    Dockerfile \
    Dockerrun.aws.json \
    *.py \
    cron.yaml \
    requirements.txt \
    secret.json \
    templates/*


