#!/bin/bash
if [[ `pwd` =~ bin ]]; then 
	python3 ../test.py
else
	python3 ./test.py
fi

