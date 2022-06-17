FROM python:3.6
RUN pip install FLASK==0.11.1
WORKDIR /UI
COPY UI /UI
CMD [ "python" ,"app.py"]