# Celery POC

A simple Celery POC.

**Table of Contents**
- [Celery POC](#celery-poc)
  - [Prepare Environment](#prepare-environment)
  - [Do tests](#do-tests)
  - [Beware PRODUCTION](#beware-production)


## Prepare Environment

```bash
conda create -n celery python==3.8

conda activate celery

pip install -r requirements.txt
```

## Do tests

Run Redis
```bash
docker run --name poc-redis --rm -d -p 6379:6379 redis
```

Run Celery App
```bash
celery -A tasks worker --concurrency=1 --loglevel=INFO
```

Run invoke tasks directly
```bash
python call_task.py
# or agnostic
python agnostic_call.py
```

Run flower
```bash
celery --broker=redis://localhost:6379/0 flower
```

## Beware PRODUCTION

In production you’ll want to run the worker in the background as a daemon. To do this you need to use the tools provided by your platform, or something like [supervisord](http://supervisord.org/) (see Daemonization for more information).