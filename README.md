### Stackdriver python profiler and `Celery -P gevent` bug
#### The bug
- Instantiating Stackdriver python profiler inside `celery` workers started using `-P gevent` option would experience a hiccup during its execution.
- The hiccup happens once in a while for a duration of 10 seconds, its relation to Stackdriver python profiler are noticeable with proper log level.
#### Clues
- The hiccup duration is a consistent 10 seconds.
- Disabling CPU profiling solves the problem.
- Removing the `-P gevent` option solves the problem.
#### Reproducing the bug
1. Clone this repo.
2. `cd` into it.
4. Setup cloud profiler related stuff(credentials, project ids)
4. `docker-compose up`
5. At this point, the `dispatcher` service is dispatching tasks non-stop, meaning the worker should be logging continuously.
5. Watch for logs from the `worker` service for the hiccup.
    - The hiccup will occur after logging `Successfully created a CPU profile`.
    - Watch how for the next 10 seconds it wouldn't process/log anything. THIS IS THE BUG.
    - Then, processing/logging resumes normally after logging `Starting to upload profile`.
