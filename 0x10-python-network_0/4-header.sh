#!/bin/bash
# This script GETs & displays the body of a response, while sending a header variable.
curl -sH "X-School-User-Id: 98" "$1"
