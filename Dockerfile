FROM python:3.7-alpine

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN echo 'Launching the magic... '

WORKDIR /bot
CMD ["python3", "autoreply.py"]

COPY </Users/carlos.morales/Desktop/sabinaquotes>  <WORKDIR>
