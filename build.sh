#!/bin/bash

openapi-generator generate -i ./openapi.yaml -o ./ -g python -c ./config.json --git-repo-id foxhole-warapi-python-client --git-user-id Opa-
