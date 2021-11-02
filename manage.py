#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests
from django.shortcuts import render


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'domashno_spirka.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def transport(request):
    all_data = requests.get('https://api-v3.mbta.com/predictions?page[offset]=0&page[limit]=3&sort=-departure_time&filter[stop]=place-north').json()
    travel_data = []
    for i in all_data.get("data"):
        arr_time = i.get("attributes").get("arrival_time")
        dept_time = i.get("attributes").get("departure_time")
        direction = i.get("attributes").get("direction_id")
        route_id = i.get("relationships").get("route").get("data").get("id")
        route = requests.get('https://api-v3.mbta.com/routes/' + route_id).json()
        print(direction, route)
        destination = route["data"]["attributes"]["direction_destinations"][direction]
        train_times = [arr_time, dept_time, destination]
        travel_data.append(train_times)
    return render(request, "stranica.html", {"trains": travel_data})


if __name__ == '__main__':
    main()