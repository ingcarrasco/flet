FROM python:alpine3.19
WORKDIR /app
COPY test .
RUN pip install -r requirements.txt
EXPOSE 8550
ENTRYPOINT ["flet"] 
CMD ["run","main.py","--port", "8550","--web"]