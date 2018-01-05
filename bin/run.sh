#!/bin/bash
if [[ `pwd` =~ bin ]]; then
        python3 ../fib_py.py $*
else
        python3 ./fib_py.py $*
fi
