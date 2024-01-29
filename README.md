# Tomato AI Server

The application is a server side service to learn how to use Django Framework.

## Installation 

1. Clone the repository:
```bash
   git clone https://github.com/pieruccim/tomato-ai-server
```
2. Navigate to the project directory:
```bash
   cd tomato-ai-server
```
3. Install all dependencies:
```bash
   pip install -r requirements.txt
```
4. Run server:
```bash
   python manage.py runserver
```

### Running on Docker:

1. Navigate to the project directory with Dockerfile and docker-compose.yaml:
```bash
   cd tomato-ai-server
```
2. Build Docker image:
```bash
   docker-compose build
```
3. Run the Docker container:
```bash
   docker-compose up
```

## Running Tests
1. Navigate to the project directory with Dockerfile and docker-compose.yaml:
```bash
   cd tomato-ai-server
```
2. Run module tests:
```bash
   python manage.py test ServerPrototypeApp.module_to_test
```



