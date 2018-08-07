FROM python:3.7

# Install dependencies
ADD requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Add sample application
ADD *.py /opt/application/
ADD templates/ /opt/application/templates/
ADD secret.json /

EXPOSE 5000

# Run it
ENV FLASK_APP /opt/application/app.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
