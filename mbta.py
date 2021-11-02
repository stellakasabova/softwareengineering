import requests

def find_route_id(predictions_route_id, route):
    for i in route["data"]:
        if predictions_route_id == i["id"]:
            return i["attributes"]["direction_names"]

predictions = requests.get("https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-north").json()
routes = requests.get("https://api-v3.mbta.com/routes?filter%5Bstop%5D=place-north").json()
#schedule = requclests.get("https://api-v3.mbta.com/schedules?filter%5Bstop%5D=place-north").json()

for i in predictions["data"]:
    direction_start = find_route_id(i["relationships"]["route"]["data"]["id"], routes)[0]
    direction_end = find_route_id(i["relationships"]["route"]["data"]["id"], routes)[1]
    print(#i["attributes"]["arrival_time"] + "\t" 
        #i["attributes"]["departure_time"] + "\t" 
        i["attributes"]["status"] + "\t"
        + i["relationships"]["route"]["data"]["id"] + "\t" 
        + direction_start + " - " + direction_end)