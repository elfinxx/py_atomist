FROM alpine:3.4

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

COPY py_atomist /tmp/service/py_atomist
COPY requirements.txt /tmp/service/requirements.txt
COPY setup.py /tmp/service/setup.py

RUN cd /tmp/service && \
    pip install --no-cache-dir -r requirements.txt && \
    python3 setup.py install && \
    cd - && \
    rm -rf /tmp/service 

EXPOSE 5000

ENTRYPOINT ["python3", "-m", "py_atomist"]
CMD ["--prod"]