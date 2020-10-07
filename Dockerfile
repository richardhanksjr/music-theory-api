# Pull base image
FROM python:3.8


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set work directory
WORKDIR /code


# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv lock --clear && pipenv install --system

# Copy project
COPY . /code/

# Collect static files
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
#RUN npm install


