import requests
from celery import shared_task

from .models import PlaceHolder


@shared_task
def fetch_api():
    headers = {"Content-Type": "application/json"}
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/photos', headers=headers)
    if response.status_code == 200:
        if PlaceHolder.objects.count() == 0:
            item_id = 1
        else:
            item_id = PlaceHolder.objects.last().item_id
            item_id += 1
        try:
            json = response.json()[item_id]
            PlaceHolder.objects.create(
                item_id=json.get('id'),
                albumId=json.get('albumId'),
                url=json.get('url'),
                title=json.get('title'),
                thumbnail_url=json.get('thumbnailUrl'),
            )
            print('Task Created')
        except Exception as a:
            print(a)
            pass
    print('Task Called')
    return True
