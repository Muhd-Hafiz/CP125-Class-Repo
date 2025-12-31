Stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]

def find_station(stations, name):
    for name in range(len(stations)):
        if stations[name] == name:
            return name
        else:
            return None
    

def count_stops(stations, start, stop):
    start_station = find_station(stations, start)
    stop_station = find_station(stations, stop)
    
