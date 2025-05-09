# Use the official Python image as the base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install Poetry and dependencies
RUN pip install poetry && poetry install

# Expose the port the app will run on
EXPOSE 8080

# Run the app
CMD ["poetry", "run", "python", "main.py"]
