# Specifying the platform is optional but helps eliminate a source of error
# x86_64 is what PCs and Intel Macs use
# arm64 is what Apple Silicon Macs uses by default
# Appl Silicon macs can also run x86_64 images if Rosetta 2 is installed
FROM --platform=x86_64 python:3.10-slim-buster

# Set the working directory in the container so we know where we are
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Pip install
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "script.py"]
