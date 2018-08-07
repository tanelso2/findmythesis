FROM python:3.7

# Add sample application
ADD *.py /opt/application/
ADD requirements.txt /
ADD templates/ /opt/application/templates/
ADD secret.json /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

EXPOSE 5000

# Run it
ENV FLASK_APP /opt/application/app.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
