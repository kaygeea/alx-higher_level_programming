#!/bin/bash
# This script sends a POST request to a given URL and displays the body of the response.
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
