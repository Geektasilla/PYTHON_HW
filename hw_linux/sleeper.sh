#!/bin/bash
for i in {1..10}
do
    echo "$(date +"%H:%M:%S") $(ps -e | wc -l)"
   # sleep 5
done

lscpu > info.txt; cat /etc/os-release | grep "^NAME=" | tr -d '"' >> info.txt; cat /etc/os-release | grep "^NAME=" | cut -d= -f2 | tr -d '"' >> info.txt

for n in {50..100}
do
    touch "hw_15/${n}.txt"
done
