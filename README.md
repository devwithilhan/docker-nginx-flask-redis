# Docker Nginx Flask Redis

A beginner-friendly Docker Compose project demonstrating how multiple containers communicate with each other.

## Technologies

- Docker
- Docker Compose
- Nginx
- Flask
- Redis

## Architecture

```
Browser
    │
    ▼
 Nginx (Reverse Proxy)
    │
    ▼
 Flask Application
    │
    ▼
 Redis
```

## Project Structure

```
docker-nginx-flask-redis/
│
├── docker-compose.yml
│
├── flask/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── nginx/
│   └── default.conf
│
└── redis/
    ├── Dockerfile
    └── redis.conf
```

## Features

- Docker Compose
- Reverse Proxy with Nginx
- Flask Web Application
- Redis Integration
- Persistent Redis Volume

## Getting Started

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/docker-nginx-flask-redis.git
```

Start the application

```bash
docker compose up --build
```

Open your browser

```
http://localhost:7081
```

## Available Routes

| URL | Description |
|------|-------------|
| / | Welcome page |
| /visits | Visitor counter |
| /visits/reset | Reset visitor counter |
| /health | Health endpoint |

## How it works

1. The browser sends a request to Nginx.
2. Nginx forwards the request to the Flask container.
3. Flask processes the request.
4. Flask stores and retrieves data from Redis.
5. Flask sends the response back through Nginx to the browser.

## Learning Goals

This project was created to learn:

- Docker Images
- Docker Compose
- Volumes
- Container Networking
- Reverse Proxy
- Redis Basics

## Future Improvements

- Load Balancing
- Health Checks
- Custom Error Pages
- HTTPS
- Kubernetes Deployment