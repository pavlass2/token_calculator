# Build like this:
# docker build -t token_calculator .


# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start the Uvicorn server
CMD ["uvicorn", "web_service:app", "--host", "0.0.0.0", "--port", "8000"]