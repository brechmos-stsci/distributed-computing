# distributed-computing
An area to document code for distributed-computing

Basic view of distributed computing...

![](https://raw.githubusercontent.com/brechmos-stsci/distributed-computing/master/images/distributed.jpeg)
from http://slideplayer.com/slide/7076521/

## Dask

[Dask distributed](https://distributed.readthedocs.io/en/latest/quickstart.html)

* Client - where we run our main script

* Proxy - Scheduler process

* Server - Worker process(es) `$ dask-worker`

## Celery

[Celery Distributed Task Queue](http://www.celeryproject.org)

* Client - where we run our main script

* Proxy - "Broker" which can be Redis or RabbitMQ (essentially a key-value store)

* Server - Worker process(es) `$ celery worker`
