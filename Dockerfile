FROM python:3.7-slim

RUN apt-get update

COPY ./smart_design_store /app/smart_design_store
COPY ./tests /app/tests
COPY ./setup.py /app/setup.py

WORKDIR /app

RUN pip install --upgrade setuptools
RUN pip install -e /app

CMD ["python", "-m", "smart_design_store"]
