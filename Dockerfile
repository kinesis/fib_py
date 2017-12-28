FROM python:3
ADD ./ ./
MAINTAINER mail@kinesis.me

# install virtual env python and pip
RUN mkdir -p venv
RUN pip3 install virtualenv 
RUN python3 -m virtualenv ./venv
RUN /bin/bash -c -l "source ./venv/bin/activate"

# run tests
CMD python3 ./fib_test.py
 
