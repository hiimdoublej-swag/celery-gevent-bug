# -*- coding: utf-8 -*-
import os
import time

import googlecloudprofiler
from celery import Celery


googlecloudprofiler.start(
    service='celery-gevent-bug',
    verbose=3,
    # May comment out the following line if the value would be derived automatically.
    project_id=os.environ.get('PROFILER_PROJECT_ID')
)


app = Celery(__name__, broker='redis://redis:6379/0')


@app.task()
def test_task():
    start_time = time.time()
    while time.time() - start_time < 0.5:
        pass
