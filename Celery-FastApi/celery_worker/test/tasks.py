import logging
import time

from celery_worker.api_proxy import ServerAPI
from celery_worker.celery_config import app

from celery import shared_task


@app.task
def sample_task():
    for i in range(10):
        print(f"====== Task {i}=====")
        time.sleep(5)
        print('ba noi may')

    logging.info("Done task")


@app.task
def update_role_user(*args, **kwargs):
    url = 'http://127.0.0.1:8000/api/v1/train/user/change_roll'

    data = {
        'user_id': kwargs['user_id'],
        'role': kwargs['role']
    }

    response = ServerAPI(
        api_url=url,
        payload=data,
        token=None
    ).put()
    print(f"================_user====={url}======:{data}===={response}")
    rs = response.get('result', {})
    return rs




@shared_task
def add():
    print('========= Share task =========')
    a = 2 + 1
    print(f'{a} DONE TASK')
