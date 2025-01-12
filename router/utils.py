import math
import pandas as pd
import polyline

def euclidean_distance_km(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    distance = math.sqrt(dlat**2 + dlon**2)
    
    # Convert distance from radians to kilometers (Earth's radius ~ 6371 km)
    earth_radius_km = 6371
    distance_km = distance * earth_radius_km
    
    return distance_km


def filter_gas_stations(file_path, lat1, lon1, lat2, lon2, output_file='filtered-gas-stations.csv'):
    # Read the Excel file containing the gas station data
    df = pd.read_csv(file_path)
    
    # Find the min and max values for latitudes and longitudes
    min_lat = min(lat1, lat2)
    max_lat = max(lat1, lat2)
    min_lon = min(lon1, lon2)
    max_lon = max(lon1, lon2)
    
    # Filter gas stations that fall within the boundaries
    filtered_gas_stations = df[
        (df['latitude'] >= min_lat) & (df['latitude'] <= max_lat) &
        (df['longitude'] >= min_lon) & (df['longitude'] <= max_lon)
    ]
    
    # Save the filtered data to a new Excel file
    filtered_gas_stations.to_csv(output_file, index=False)

    print(f"Filtered gas stations: {filtered_gas_stations.shape[0]}")
    print(f"Filtered data saved to {output_file}")

    return filtered_gas_stations

# encoded_geometry = "mlpqFh|x_S{peEdDqd@lbc@auGjqJuxfAt|cAwu_@hbEukCtk]c_Ob_d@y_ThgXsif@laqAjrC~fc@cmJtzeChb^dinD{oB`omAi}G`za@n|Qv~w@coAfrKfbNlk\\zt@fvLw}FhsS`aCdafAb}_@dh_AvbN`|{@meAfjb@t~Ft{Q|}Bhnl@p`VthQ~~]xju@hoZagHb`T`vWurEppKplFpj}@ohGm~@"
def decode_geometry(encoded_geometry):
    decoded_points = polyline.decode(encoded_geometry)

    return decoded_points
