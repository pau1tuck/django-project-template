# Dockerfile
# Use the official Redis image from Docker Hub
FROM redis:latest

# Set the default Redis configuration file
COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose Redis default port
EXPOSE 6379

# Run Redis with the configuration file
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
