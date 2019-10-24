FROM python:3.6.9-alpine

RUN pip install web.py

COPY templates /src/templates
COPY *.py /src/

WORKDIR /src

EXPOSE 8080
CMD ["python3", "code.py"]
