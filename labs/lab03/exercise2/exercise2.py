def find_station(stations, name):
    for i in range(len(stations)):
        if stations[i] == name:
            return i
    return None

def count_stops(stations, start, stop):
    start_station = find_station(stations, start)
    stop_station = find_station(stations, stop)
    if start_station == None or stop_station == None:
        return -1
    return abs(stop_station - start_station)
