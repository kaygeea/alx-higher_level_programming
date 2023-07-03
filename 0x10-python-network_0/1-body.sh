#!/bin/bash
# This script takes a URL, GETs and diplays body of response for ONLY requests with 200 status code response.
curl -sL "$1"
