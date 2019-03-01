FROM python:3.7-alpine

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Install pipenv
RUN pip3 install pipenv

# Set working directory and copy Pipfiles
WORKDIR /app/src
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# Install application dependencies
RUN apk add --no-cache --virtual .build-deps \
      mariadb-dev build-base musl-dev linux-headers && \
      pipenv install --deploy --system && \
      apk add --virtual .runtime-deps nginx supervisor uwsgi-python3 mariadb-client py-mysqldb && \
      apk del .build-deps

# Copy source
COPY . .

# Setup nginx
COPY ./deployment/nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /spool/nginx /tmp/pid && \
      chmod -R 777 /var/log/nginx /etc/nginx /var/run /tmp /tmp/pid /spool/nginx && \
      chgrp -R 0 /var/log/nginx /etc/nginx /var/run /tmp /tmp/pid /spool/nginx && \
      chmod -R g+rwX /var/log/nginx /etc/nginx /var/run /tmp /tmp/pid /spool/nginx && \
      rm /etc/nginx/conf.d/default.conf

# Copy base uWSGI ini file to enable default dynamic uwsgi process number
RUN mkdir /etc/uwsgi/apps-enabled
COPY ./deployment/uwsgi.ini /etc/uwsgi/conf.d/uwsgi.ini
COPY ./deployment/uwsgi.ini /etc/uwsgi/apps-enabled/uwsgi.ini

# Setup supervisord
COPY ./deployment/supervisord.conf /etc/supervisord.conf
RUN mkdir /var/log/supervisor && touch /var/log/supervisor/supervisord.log

# Setup entrypoint
COPY ./deployment/entrypoint.sh /usr/local/bin/entrypoint.sh

# https://github.com/moby/moby/issues/31243#issuecomment-406879017
RUN ln -s /usr/local/bin/entrypoint.sh / && \
    chmod 777 /usr/local/bin/entrypoint.sh && \
    chgrp -R 0 /usr/local/bin/entrypoint.sh && \
    chown -R nginx:root /usr/local/bin/entrypoint.sh

# https://docs.openshift.com/container-platform/3.3/creating_images/guidelines.html
RUN chgrp -R 0 /var/log /var/cache /tmp/pid /spool/nginx /var/run /tmp /etc/uwsgi /etc/nginx && \
    chmod -R g+rwX /var/log /var/cache /tmp/pid /spool/nginx /var/run /tmp /etc/uwsgi /etc/nginx && \
    chown -R nginx:root /app/src && \
    chmod -R 777 /app/src /etc/passwd

EXPOSE 5000

CMD ["sh", "/usr/local/bin/entrypoint.sh", "supervisord"]

