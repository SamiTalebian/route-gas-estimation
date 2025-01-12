from rest_framework import serializers

from router.utils import filter_gas_stations
from .models import GasStationRoute

class LocationPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStationRoute
        fields = ['longitude_start', 'longitude_end', 'latitude_start', 'latitude_end']

    def save(self, **kwargs):
        instance : GasStationRoute = super().save(**kwargs)
        route = instance.fetch_route()

        # Example: Filter gas stations and move vehicle along route
        filtered_gas_stations = filter_gas_stations(
            "fuel-prices-with-coordinates.csv",
            instance.latitude_start,
            instance.longitude_start,
            instance.latitude_end,
            instance.longitude_end
        )

        instance.vehicle_move_function(route)
        return instance
