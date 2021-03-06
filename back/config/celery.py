import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-day_update_cars_mileage': {
        'task': 'cars.tasks.update_cars_mileage',
        'schedule': crontab(minute=0, hour=0),
    },
    'every-day_calculate_next_fix_date': {
        'task': 'cars.tasks.calculate_next_fix_date',
        'schedule': crontab(minute=0, hour=0),
    },
    'every-day_update_latest_fix_data': {
        'task': 'services.tasks.update_latest_fix_data',
        'schedule': crontab(minute=1, hour=0),
    },
    'every-day_calculate_predicted_fix_data': {
        'task': 'services.tasks.calculate_predicted_fix_data',
        'schedule': crontab(minute=2, hour=0),
    },
    'every-day_send_service_reminder': {
        'task': 'services.tasks.send_service_reminder',
        'schedule': crontab(minute=0, hour=0),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
