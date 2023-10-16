# Multi Application Python Demo Structure

This multirepo has a few Python projects. These projects are detailed below.
This project can be used for testing purposes and POC.

> Contained projects are simple in purpose. These projects must not be used as project templates.

**Table of Contents**
- [Multi Application Python Demo Structure](#multi-application-python-demo-structure)
  - [Projects](#projects)
    - [celery\_tasks](#celery_tasks)
    - [celery\_cron\_jobs](#celery_cron_jobs)
    - [rest\_api](#rest_api)
  - [Deploy](#deploy)
  - [Appendix - Example of Celery](#appendix---example-of-celery)


## Projects

### celery_tasks

The celery_tasks project has defined 3 simple example task for testing. This tasks are:
  * Concatenate 2 or 3 strings.
  * Calculate the exponential of a number.
  * Calculate the square root of a number.

These tasks have an active wait function that depends on an environment variable called `TASK_ARTIFICIAL_DELAY`.

### celery_cron_jobs

With a periodic time defined by the environment variable `CRON_TASK_DELAY`, this project call a task automatically.

This task is a simple print with the content of the environment variable.

### rest_api

To use the tasks defined fro this celery app, a REST API was implemented. This API have the following endpoints:
  * POST /call_task -> This endpoint can invoke one of the tasks defined in `celery_tasks` by the following structure:
    ```json
    {
      "task_name": "sqrt",
      "parameters": [
        4
      ]
    }
    ```
  * GET /task/{task_id} -> Recover the status and the result of the task with that ID.
  * GET /health-check -> Returns a dummy JSON with the state of the server.


## Deploy

All this projects can be deployed by the command
```bash
docker compose up
```

This file contains services for:
  * The broker (rabbitmq).
  * The backend (redis).
  * The celery worker, which has beat implemented (command for periodic task).
  * The REST API, exposed in port 8000.
  * The flower server, exposed in port 5556.

> All the necessary environment variables will be allocated in the `.env` file.

> To modify the config from the celery app update `celeryconfig.py`.

## Appendix - Example of Celery

There is a functional celery example in folder `_experimental/celery_poc`.

This folder can be used for celery testing purposes.