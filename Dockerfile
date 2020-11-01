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

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN npm install
RUN npm install babel-core@^7.0.0-bridge.0 --save-dev --dev jest --save-dev vue-jest vue-template-compiler --save-dev jest-serializer-vue -g yarn
#RUN npm run dev

# Collect static files
RUN python manage.py collectstatic --noinput