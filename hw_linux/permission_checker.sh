#!/bin/bash

DIR=/opt/101025-ptm
ls -la $DIR | grep -v total | awk '{print $1}'

for i in $DIR/*
  do
    if [[ "$i" == *.sh ]]; then
    chmod +x $i
    fi
done	
