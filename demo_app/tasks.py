from demo.celery import app


class AddClass(app.Task):
    def run(self):
        print('run')


app.tasks.register(AddClass)


@app.task
def demo_task():
    print('demo_task')


app.tasks.register(demo_task)
