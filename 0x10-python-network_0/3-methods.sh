#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
