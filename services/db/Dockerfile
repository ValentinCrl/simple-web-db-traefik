FROM postgres:16-alpine

# Simple healthcheck-friendly init
COPY init.sql /docker-entrypoint-initdb.d/01-init.sql
