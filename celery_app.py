from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend='redis://localhost:6379/0',  # Replace with your Redis backend URL
        broker='redis://localhost:6379/0'   # Replace with your Redis broker URL
    )
    celery.conf.update(app.config)
    return celery