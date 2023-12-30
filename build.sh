#!/bin/bash

swagger-codegen generate -i ./openapi.yaml -o ./ -l python -c ./config.json
