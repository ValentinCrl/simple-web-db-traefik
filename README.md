# Simple Web + DB with Traefik (HTTPS) — build & push via Docker Compose

This template gives you a minimal Python Flask app + PostgreSQL, fronted by Traefik v2 with automatic HTTPS (Let's Encrypt).  
Images are **built locally from compose** and can be **pushed to Docker Hub** with `docker compose push`.

## 1) Prereqs
- DNS **A record** for your domain pointing to this server (e.g. `app.yourdomain.tld` → public IP).
- Docker & Docker Compose.
- `docker login` to Docker Hub.

## 2) Configure
Copy the example and edit:
```bash
cp .env.example .env
# edit .env: DOCKERHUB_USER, IMAGE_TAG, DOMAIN, ACME_EMAIL, DB creds
```

## 3) Build (locally) and run
```bash
docker compose build
docker compose up -d
```

Open: `https://${DOMAIN}`

## 4) Push images to Docker Hub
```bash
docker compose push
```

## Notes
- If you are on ARM but want amd64 images:  
  `DOCKER_DEFAULT_PLATFORM=linux/amd64 docker compose build`
- Traefik certificates stored under `./letsencrypt/acme.json`.
- Traefik dashboard is exposed at `https://traefik.${DOMAIN}`.

## Troubleshooting
- Check logs:
  ```bash
  docker compose logs -f traefik
  docker compose logs -f app
  docker compose logs -f db
  ```
