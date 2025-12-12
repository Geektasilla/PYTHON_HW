#!/bin/bash

DIR="/opt/101025-ptm/viktoria_mariella/giktozilla"

DATE=$(date +%d.%m.%Y)

for i in {1..10}
  do
    echo "created: $(date '+%d.%m.%Y %H:%M:%S')" > "$DIR/${i}_${DATE}"
   sleep 2
  done 

