import logging

from fastapi import FastAPI

from celery_worker.ok import ok
from celery_worker.test.tasks import sample_task, update_role_user

app = FastAPI()


@app.get("/test")
def test():
    print('-------Start job------')
    return ok()
    return {'MESSAGE': 'Ma cha co noi nha may tien su dong ho nha may =)))ggggfgf'}



@app.get("/test_2")
def test2():
    print('234')
    update_role_user(user_id="A9AAC4D5BBF24FF382722498D524C51E",role=1).apply_async()
    logging.info("end---gameee")
    print("gi vay cha")
    return {'MESSAGE': 'Task Submitted'}