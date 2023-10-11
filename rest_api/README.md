# REST API

# Antia tasks

* Create a `requirements.txt` file with at least FastAPI.
* Create a simple FastAPI that has the following endpoints:
  * POST /call_task -> with a JSON body to invoke one of the tasks defined in `celery_tasks`
  * GET /task/{task_id} -> recover the status and (if possible) the result of an operation
  * GET /health-check -> returns a dummy JSON with the state of the server.
* Create Dockerfile
* Include this Dockerfile into ../docker-compose-yml
* Replace this README.md