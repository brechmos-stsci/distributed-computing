from __future__ import absolute_import, unicode_literals
from celery import Celery

#
# Setup the actual celery app which is used
# in a few other parts of the code.  Main thing
# here is we need to define who to talk to in 
# order to disseminate jobs and look for jobs.
#
app = Celery('transfer_learning',
             broker='redis://',
             backend='redis://',
             include=[
                 'summer',
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
