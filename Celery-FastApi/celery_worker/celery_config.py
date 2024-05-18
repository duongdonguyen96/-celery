from celery import Celery

from celery.schedules import crontab

app = Celery(
    'celery_fastapi',
    broker='amqp://guest:guest@rabbitmq:5672/vhost',
    include=[
        'celery_worker.test.tasks'
    ])

app.conf.beat_schedule = {
    'add': {
        'task': 'celery_worker.test.tasks.add',
        'schedule': crontab(minute='*/10'),
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
