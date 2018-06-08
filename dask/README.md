# Introduction

Dask has a focus on advanced parallelism for analytics (they talk about numpy, Pandas, Scikit-Learn on their website). 

> Dask is a flexible parallel computing library for analytic computing.

These are notes on how to get Dask running on a computer or multiple computers.

https://distributed.readthedocs.io/en/latest/quickstart.html

Essentially there are three parts to the Dask system:  
  * Submitter - this computer/program one submits the jobs
  * Scheduler - a process that runs on a computer that acts as a broker between the submitter and the workers
  * Worker(s) - process(es) that do the actual work received from the scheduler.

# Setup

The following need to be installed

```
pip install dask distributed --upgrade
```


# Quickstart

1) Start the schedulre before running the runme.py:

```
$ dask-scheduler
```

2) Start up the workers on the local or remote machines:

```
$ dask-worker 127.0.0.1:8786
$ dask-worker 127.0.0.1:8786
```

Then, once the scheduler and workers are going we can run the program that requires distribution.
