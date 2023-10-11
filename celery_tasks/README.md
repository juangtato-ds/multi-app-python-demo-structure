# Celery Tasks

# Antia tasks

* Create a `requirements.txt` file with celery to use both redis and rabbitmq.
* Create celery app
  * This task should pick configuration from environment variables.
  * Broker must be RabbitMQ
  * Backend must be Redis
* Create at least 3 celery tasks where:
  * There can be a env variable called `TASK_ARTIFICIAL_DELAY` that may contain a number a of seconds to make an active wait inside the task
  * Define input for the task (as you like)
  * Perform an operation over input parameters (as you like)
* Create Dockerfile
* Include this Dockerfile into ../docker-compose-yml
* Replace this README.md