#!/bin/bash
echo "Hello $USER"
date
echo $PWD
process_bioset=$(ps -ef | grep -v grep | grep bioset | wc -l)
echo "bioset process count $process_bioset"
ls -la /etc/passwd | awk '{print $1}' 

