FROM python:3.7-alpine

COPY bot/config.py /bot/
COPY bot/favretweet.py /bot/
COPY bot/autoreply.py /bot/

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "autoreply.py"]
