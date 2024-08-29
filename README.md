# Project Documentation

## Overview

This Django project is designed for a technical test by DevGrid and includes a web application that collects data from the Open Weather API.

- To use the application: `http://3.142.140.39:3000/`

- The API documentation with Swagger is available on the application's index page.

## Architecture

The project utilizes the following technologies: Back-End in Python and Django, SQLite database, Celery for asynchronous tasks, Redis as the message broker, and an AWS EC2 instance for hosting with Amazon Linux OS. The project is containerized using Docker, with Docker Compose for orchestration.

### Sequence Diagram

![Sequence Diagram](doc_images/sequence_diagram.png)

## Project Structure

- **`weather_api_wrapper/`**: Main directory of the Django project.
  - **`settings.py`**: Main configuration file for Django.
  - **`celery.py`**: Configuration file for the Celery application.
  - **`urls.py`**: Global routing file for the project.
- **`weather/`**: API code for the project.
  - **`urls.py`**: Global routing of API URLs.
  - **`models.py`**: Model definitions.
  - **`views.py`**: Business logic and requirements.
  - **`tests.py`**: Unit tests.
- **`cities_list.py`**: List of city IDs, extracted from the appendix of the technical test.
- **`Dockerfile`**: Defines the Docker image for the application.
- **`docker-compose.yml`**: Configuration for orchestrating Docker containers.
- **`.env`**: Environment variables, with Open Weather API Key.
- **`run.sh`**: Script to start Docker containers.
- **`requirements.txt`**: List of Python dependencies for the project.

## API Key Configuration

   - Update the `.env` file with your Open Weather API key:

     ```bash
     OPEN_WEATHER_API_KEY={your_api_key}
     ```

## Running the Application

### Prerequisites:

- Python 3.10
- Redis Server
- Celery
- Docker
- Docker Compose

### Option 1: `run.sh`

The `run.sh` script is used to start the Docker containers easily.

- Make the `run.sh` script executable (only necessary once):

```bash
chmod +x run.sh
```

- After that, simply run the script.

```bash
sudo ./run.sh
```

### Option 2: Manual Commands

```bash
sudo docker-compose build
sudo docker-compose up -d
```

After that, your project will be available at `http://127.0.0.1:3000`

### Running Tests

To run the unit tests on the project's API, execute the following command while the application is running:

```bash
sudo docker exec weather_api_wrapper python3 manage.py test
```