FROM python:3.11-alpine

# Update installation utility
RUN apk update
RUN apk upgrade
RUN apk add dumb-init

# Environment variables
ENV TZ=America/New_York

# Create working directory
RUN mkdir /app
WORKDIR /app

# Install the requirements
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# dumb init for mounts
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# Run the server on container startup
CMD [ "python", "-u","slackbotExercise.py"]
