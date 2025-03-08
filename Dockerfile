# Use Python 3.13.2 as the base image
FROM python:3.13.2

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including src/ where run.py is located)
COPY . .

# Set the working directory inside the container to src/
WORKDIR /app/src

# Expose the application port (optional, only if needed)
EXPOSE 8000

# Run the Python script
CMD ["python", "run.py"]