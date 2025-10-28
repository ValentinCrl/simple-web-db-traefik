#!/usr/bin/env bash
set -euo pipefail

if [ ! -f .env ]; then
  echo "Create and fill .env first (cp .env.example .env)"; exit 1
fi

echo "==> Building images"
docker compose build

echo "==> Pushing images"
docker compose push

echo "Done."
