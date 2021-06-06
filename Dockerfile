FROM python:3.9

# Install dependencies
ADD requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Add sample application
ADD *.py /opt/application/
ADD templates/ /opt/application/templates/
ADD secret.json /opt/application

EXPOSE 5000

# Run it
WORKDIR /opt/application
CMD gunicorn --bind 0.0.0.0:5000 --worker-class aiohttp.worker.GunicornWebWorker app:app
