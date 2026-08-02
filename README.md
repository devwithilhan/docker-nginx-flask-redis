# Docker Nginx Flask Redis

A beginner-friendly Docker Compose project demonstrating how multiple containers communicate with each other using a reverse proxy and custom Docker images.

## Technologies

- Docker
- Docker Compose
- Nginx
- Flask
- Redis

## Architecture

```text
Browser
    │
    ▼
Nginx (Reverse Proxy + Load Balancer)
    │
    ├────────► Flask 1
    ├────────► Flask 2
    └────────► Flask 3
                  │
                  ▼
                Redis
```

## Project Structure

```text
docker-nginx-flask-redis/
│
├── compose.yaml
│
├── flask/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
│
└── redis/
    ├── Dockerfile
    └── redis.conf
```

## Features

- Docker Compose orchestration
- Custom Docker images
- Nginx reverse proxy
- Nginx load balancing
- Flask web application
- Redis integration
- Persistent Redis volume
- Container networking

## Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/docker-nginx-flask-redis.git
```

Build and start the containers:

```bash
docker compose up --build
```

Open your browser:

```text
http://localhost:7081
```

## Available Routes

| URL | Description |
|------|-------------|
| / | Welcome page |
| /visits | Visitor counter |
| /visits/reset | Reset visitor counter |
| /health | Health endpoint |

## How It Works

1. The browser sends a request to the Nginx container.
2. Nginx acts as a reverse proxy and forwards the request to the Flask application.
3. Flask processes the request.
4. Redis stores the visitor counter.
5. Flask returns the response through Nginx back to the browser.

## Learning Goals

This project was built to practice:

- Building custom Docker images
- Docker Compose
- Container networking
- Docker volumes
- Reverse proxies with Nginx
- Redis basics
- Multi-container applications

## Future Improvements

- Health checks
- Custom Nginx error pages
- HTTPS with TLS certificates
- Docker Compose profiles
- CI/CD with GitHub Actions
- Kubernetes deployment