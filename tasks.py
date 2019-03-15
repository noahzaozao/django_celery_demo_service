from celery import task


@task
def demo_task():
    print('demo_task')
