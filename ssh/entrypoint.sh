#!/bin/bash

service ssh start
ssh-keygen -f ~/.ssh/mysecret_rsa -t rsa -N ''
bash