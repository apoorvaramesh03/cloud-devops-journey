# Docker Flask Application

## Objective

This project demonstrates how to containerize a simple Python Flask application using Docker.

---

## Project Structure

```
docker-flask-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Technologies Used

- Python
- Flask
- Docker

---

## Docker Commands

### Build the Docker Image

```bash
docker build -t docker-flask-app .
```

### Run the Container

```bash
docker run -d -p 5000:5000 --name flask-container docker-flask-app
```

### View Running Containers

```bash
docker ps
```

### Stop the Container

```bash
docker stop flask-container
```

### Start the Container

```bash
docker start flask-container
```

---

## Application

Open your browser and visit:

```
http://localhost:5000
```

---


## What I Learned

- Created a simple Flask application
- Wrote a Dockerfile
- Built a Docker image
- Ran a Flask application inside a Docker container
- Used basic Docker commands

---

## Future Improvements

- Add HTML templates
- Add CSS styling
- Push the Docker image to Docker Hub
- Deploy the application to Azure

---

