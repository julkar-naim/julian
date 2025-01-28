FROM python:3.10.15-bullseye

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create non-root user
RUN groupadd -g 900 mesop && useradd -u 900 -s /bin/bash -g mesop mesop
USER mesop

# Add app code here
COPY . /srv/mesop-app
WORKDIR /srv/mesop-app

# Run Mesop through gunicorn. Should be available at localhost:8080
EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "ui:me"]