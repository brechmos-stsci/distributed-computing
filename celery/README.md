# Introduction

> Celery is an asynchronous task queue/job queue based on distributed message passing.    It is focused on real-time operation, but supports scheduling as well.
> 
> The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet, or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).


These are notes on how to get Celery running on a computer or multiple computers.

http://www.celeryproject.org

Essentially there are three parts to the Celery system:  
  * Submitter - this computer/program one submits the jobs
  * Scheduler - a process that runs on a computer that acts as a broker between the submitter and the workers
  * Worker(s) - process(es) that do the actual work received from the scheduler.

# Setup

The following need to be installed

```
pip install celery --upgrade
```


# Quickstart

1) Startup a key-value store, such as redis. What I did is went to `https://redis.io/download` and downloaded redis, untarred it, compiled and then ran it. Nothing magical.


```
$ ./redis-server
```

2) Setup the configuration file. *This is the hardest part in my mind.*

```
from __future__ import absolute_import, unicode_literals
from celery import Celery

#
# Setup the actual celery app which is used
# in a few other parts of the code.  Main thing
# here is we need to define who to talk to in
# order to disseminate jobs and look for jobs.
#
app = Celery('celery-demo',
             broker='redis://',
             backend='redis://',
             include=[
                 'celery_smoother',
             ])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_TASK_SERIALIZER='pickle',
    CELERY_RESULT_SERIALIZER='pickle',
    CELERY_ACCEPT_CONTENT=['pickle', 'json']
)

if __name__ == '__main__':
    app.start()
```

3) Start up the workers on the local or remote machines:

```
$ celery -A celery_conf worker --loglevel=info -c 3
```

So, this command could be run on several machines to start up workers on multiple systems.

The only caveat is they will need access to teh redis queue defined in the configuration file in Step 2.

