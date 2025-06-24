FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies (like awscli)
# Combine apt update and apt install in a single RUN command
RUN apt-get update -y && apt-get install -y awscli \
    && rm -rf /var/lib/apt/lists/* # Clean up apt cache to reduce image size

# Copy the rest of your application code
COPY . .

# Expose the port your application listens on (assuming 8080 from your docker run command)
EXPOSE 8080

# Define the command to run your application
CMD ["python3", "app.py"]
