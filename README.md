# Docker Compose Template

Bare-bones template for Docker Compose, with single app directory. Includes a frontend, a redis-queue and a backend-worker.

## Setup

Create a Docker network on the host.

```bash
$ docker network create my_network
```

Creating an external network will allow other Docker applications on the same network to speak with this one. This allows us to, for example, run Nginx off of a separate compose file.

## Run

Spin up by running:

```bash
$ docker-compose up
```

Then browse to at <http://localhost:5000/>
