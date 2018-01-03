#!/bin/bash
if [[ `pwd` =~ bin ]]; then 
	python3 ../fib_test.py
else
	python3 ./fib_test.py
fi

