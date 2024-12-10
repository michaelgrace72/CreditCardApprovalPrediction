# Use a slim base image to minimize size
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
COPY app.py .
COPY catboost_model.cbm .
COPY catboost_model2.cbm .
COPY templates ./templates
COPY static ./static

# Install dependencies using pip and clean up to reduce layer size
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app will run on
EXPOSE 5000

# Define the command to run your Flask application
CMD ["flask", "run", "--host=0.0.0.0"]