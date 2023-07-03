#!/bin/bash
# This script displays all HTTP methods that the server of a passed URL will accept
curl -sI "$1" -X "OPTIONS" | grep "Allow" | cut -c8-
