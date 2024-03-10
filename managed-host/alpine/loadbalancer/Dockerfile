# Use alpine-systemd as base image
FROM alpine-systemd as loadbalancer
# Use jrei/systemd-alpine as base image
# FROM jrei/systemd-alpine as loadbalancer

# Rest of your Dockerfile...

# Install necessary packages
RUN apk update && \
    apk add bash git openssh rsync augeas shadow nginx && \
    deluser $(getent passwd 33 | cut -d: -f1) && \
    delgroup $(getent group 33 | cut -d: -f1) 2>/dev/null || true && \
    mkdir -p ~root/.ssh /etc/authorized_keys && chmod 700 ~root/.ssh/ && \
    augtool 'set /files/etc/ssh/sshd_config/AuthorizedKeysFile ".ssh/authorized_keys /etc/authorized_keys/%u"' && \
    echo -e "Port 2226\n" >> /etc/ssh/sshd_config && \
    cp -a /etc/ssh /etc/ssh.cache && \
    rm -rf /var/cache/apk/*

# Expose port 2226 for SSH and port 80 for Nginx
EXPOSE 2226 80

# Copy the entrypoint script
COPY docker-entrypoint.sh /entry.sh
RUN chmod a+x /entry.sh
ENTRYPOINT ["/entry.sh"]

# Start SSH and Nginx
CMD ["/usr/sbin/sshd", "-D", "-e", "-f", "/etc/ssh/sshd_config", "&&", "nginx", "-g", "'daemon off;'"]
# CMD /usr/sbin/sshd -D -e -f /etc/ssh/sshd_config && nginx -g 'daemon off;'