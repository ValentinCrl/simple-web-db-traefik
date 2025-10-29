FROM postgres:16-alpine AS db

# Simple healthcheck-friendly init
COPY init.sql /docker-entrypoint-initdb.d/01-init.sql
