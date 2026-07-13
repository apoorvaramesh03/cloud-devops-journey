# Docker HTML Application

## Objective

Learn Docker by containerizing and running a static HTML website using Nginx.

---

## Architecture

Browser
    │
    ▼
Docker Container
    │
    ▼
Nginx Web Server
    │
    ▼
index.html

---

## Project Structure

docker-html-app/
├── Dockerfile
├── index.html
├── README.md
└── screenshots/

---

## Technologies Used

- Docker
- Nginx
- HTML

---

## Docker Commands

### Build Image

```bash
docker build -t docker-html-app .
```

### Run Container

```bash
docker run -d -p 8080:80 --name docker-html-container docker-html-app
```

### View Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop docker-html-container
```

---

## Learning Outcomes

- Understood Docker images
- Understood Docker containers
- Built a custom Docker image
- Hosted a website inside a container

---

## Future Improvements

- Add CSS
- Add JavaScript
- Push image to Docker Hub
- Deploy to Azure App Service

---

## Status

Completed