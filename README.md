# Multi Application Python Demo Structure

This multirepo has a few Python projects. These projects are detailed below.
This project can be used for testing purposes and POC.

> Contained projects are simple in purpose. These projects must not be used as project templates.

**Table of Contents**
- [Multi Application Python Demo Structure](#multi-application-python-demo-structure)
  - [Antia Tasks](#antia-tasks)
    - [Links](#links)
  - [Projects](#projects)
    - [celery\_tasks](#celery_tasks)
    - [celery\_cron\_jobs](#celery_cron_jobs)
    - [rest\_api](#rest_api)
  - [Appendix - Example of Celery](#appendix---example-of-celery)

## Antia Tasks

* Create a docker-compose-yml
  * With a Redis -> expose default port (testing purposes)
  * With a RabbitMQ -> expose default port (testing purposes)
* Complete project `celery_tasks` (check [its README](./celery_tasks/README.md))
* Complete project `celery_cron_jobs` (check [its README](./celery_cron_jobs/README.md))
* Complete project `rest_api` (check [its README](./rest_api/README.md))
* Include a Flower server to the docker-compose with the proper configuration.
* Modify `docker-compose.yml` to only expose `rest_api` port.
* Review this README.md

### Links
* Celery - https://docs.celeryq.dev/en/stable/index.html
* Celery brokers and backends - https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html
* Celery CRON tasks - https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
* Flower (its a simple dashboard for Celery) - https://flower.readthedocs.io/en/latest/


## Projects

### celery_tasks

TODO pending

### celery_cron_jobs

TODO pending

### rest_api

TODO pending

## Appendix - Example of Celery

There is a functional celery example in folder `_experimental/celery_poc`.

This folder can be used for celery testing purposes.