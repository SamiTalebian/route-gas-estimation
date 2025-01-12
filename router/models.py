from django.db import models
import pandas as pd
import requests

from router.utils import decode_geometry, euclidean_distance_km

OSRM_BASE_URL = "http://router.project-osrm.org/route/v1/driving"

class GasStationRoute(models.Model):
    longitude_start = models.FloatField()
    longitude_end = models.FloatField()
    latitude_start = models.FloatField()
    latitude_end = models.FloatField()
    total_cost = models.FloatField(default=0)

    def _find_cheapest_fuel_station(self, point, distance_limit=30, file_path="fuel-prices-with-coordinates.csv"):
        df = pd.read_csv(file_path)
        df['Coordinates'] = df['Coordinates'].apply(lambda coord: tuple(map(float, coord.split(', '))))
        nearby_stations = df[
            df['Coordinates'].apply(
                lambda station: euclidean_distance_km(point[0], point[1], station[0], station[1]) <= distance_limit
            )
        ]
        cheapest_station = nearby_stations.loc[nearby_stations['Retail Price'].idxmin()]
        return cheapest_station

    def _update_new_location(self, cheapest_station):
        self.latitude_start = cheapest_station['Coordinates'][0]
        self.longitude_start = cheapest_station['Coordinates'][1]
        self.save()

    def _fill_gas(self, point, distance_limit=30, file_path="fuel-prices-with-coordinates.csv"):
        station_point = self._find_cheapest_fuel_station(point, distance_limit, file_path)
        self._update_new_location(station_point)
        return station_point['Retail Price']

    def _check_gas_needed(self, point, limit=780): # 500 miles -> 804 km
        distance_km = euclidean_distance_km(self.latitude_start, self.longitude_start, point[0], point[1])
        return distance_km >= limit

    def vehicle_move_function(self, route):
        geometry_points = decode_geometry(route['geometry'])
        for point in geometry_points:
            if self._check_gas_needed(point):
                price_to_pay = self._fill_gas(point)
                self._add_gas_price_to_cost(price_to_pay)

    def fetch_route(self):
        url = f"{OSRM_BASE_URL}/{self.longitude_start},{self.latitude_start};{self.longitude_end},{self.latitude_end}?overview=full"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["routes"][0]

    def _add_gas_price_to_cost(self, price):
        self.total_cost += price * 50 # Assuming the price is for each gallon
        self.save()
