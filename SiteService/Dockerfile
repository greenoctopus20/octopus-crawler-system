FROM python:3.10

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Bundle app source
COPY . .

# Expose port
EXPOSE 8000

CMD ["python", "manage.py", "runserver" , "0.0.0.0:8000"]
