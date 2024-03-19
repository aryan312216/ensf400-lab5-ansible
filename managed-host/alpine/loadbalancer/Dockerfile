# Use the same base image as your app Dockerfile
FROM alpine:3.9

# Install NGINX
RUN apk add --no-cache nginx

# Copy the NGINX configuration file into the image
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start NGINX when the container launches
CMD ["nginx", "-g", "daemon off;"]