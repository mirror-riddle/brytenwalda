#!/usr/bin/bash

for file in *.py; 
    do 
        mv "$file" "${file/process_/}"
    done;