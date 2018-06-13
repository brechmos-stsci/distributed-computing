# Introduction

> Celery is an asynchronous task queue/job queue based on distributed message passing.    It is focused on real-time operation, but supports scheduling as well.
> 
> The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet, or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).
> 
> Task queues are used as a mechanism to distribute work across threads or machines.
> 
> A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform.
> 
> Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.
> 
> A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

These are notes on how to get Celery running on a computer or multiple computers.

http://www.celeryproject.org

Essentially there are three parts to the Celery system:  
  * Submitter - this computer/program one submits the jobs
  * Scheduler - a process that runs on a computer that acts as a broker between the submitter and the workers
  * Worker(s) - process(es) that do the actual work received from the scheduler.

()[https://vinta-cms.s3.amazonaws.com/media/filer_public/a4/fb/a4fbadbe-6846-4a25-863e-a040accdd69c/results_backend.jpg]


# Setup

The following need to be installed

```
pip install celery --upgrade
```


# Quickstart

1) Broker: Startup a key-value store, such as redis. What I did is went to `https://redis.io/download` and downloaded redis, untarred it, compiled and then ran it. Nothing magical.


```
$ ./redis-server
```

There are essentially 2 choices here, Redis and RabbitMQ.  Other brokers can be used and one can write their own, too.  Too much work for me, so we are going to use Redis.

2) App: The first thing to do is create a Celery instance (Celery Application or just app).  This is the entry point into everything we want to do with creating tasks or managing workers. This must be importable.

Setup the configuration file. *This is the hardest part in my mind.*

This file is `celery_conf.py`:

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

One can add other things to the configuration file such as different routes:
```
task_routes = {
    'tasks.add': 'low-priority',
}
```

or rate limiting:
```
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}
```

but that is too complex for here.

3) Worker: Start up the workers on the local or remote machines:

```
$ celery -A celery_conf worker --loglevel=info -c 3
```

So, this command could be run on the local machine -or- several machines to start up workers on multiple systems.

The only caveat is they will need access to the redis queue defined in the configuration file in Step 2.

Note the `celery_conf` part of the command, this refers back to the `celery_conf.py` file in part 2 (App).  This is how the workers figure out how to listen.

