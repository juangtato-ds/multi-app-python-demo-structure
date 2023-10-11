# Celery CRON Tasks

# Antia tasks

* Create a `requirements.txt` file with celery to use both redis and rabbitmq.
* Create celery app
  * This task should pick configuration from environment variables.
  * Broker must be RabbitMQ
  * Backend must be Redis
* Configure the celery app to run a cron task each 2 minutes (make this configurable by environment variable)
* Create Dockerfile
* Include this Dockerfile into ../docker-compose-yml
* Replace this README.md