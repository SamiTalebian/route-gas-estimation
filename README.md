# Project Title: Fuel-Optimized Route API

## Overview
This project implements a Django REST Framework (DRF) API that calculates a route between two locations in the USA and provides:
- A map of the route.
- Optimal locations to refuel along the route based on fuel prices.
- Total fuel cost assuming a vehicle efficiency of 10 miles per gallon and a maximum range of 500 miles per tank.

## Features
1. **Route Calculation**
   - Calculates the route using the OSRM (Open Source Routing Machine) API.
   - Decodes the route geometry into latitude and longitude points.

2. **Fuel Optimization**
   - Identifies optimal fuel stops within 500 miles of the current location.
   - Finds the cheapest gas station within 50 km at each stop.
   
3. **Cost Calculation**
   - Computes the total cost of fuel for the journey based on fuel prices and vehicle efficiency.

4. **RESTful API**
   - Accepts input for start and finish locations (latitude and longitude).
   - Returns the route and total fuel cost.

---

## Project Structure
```
project_root/
    |-- router/
    |    |-- admin.py
    |    |-- apps.py
    |    |-- models.py
    |    |-- serializers.py
    |    |-- views.py
    |    |-- utils.py
    |-- manage.py
    |-- requirements.txt
    |-- README.md
    |-- fuel-prices-with-coordinates.csv
```

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 3.2+
- Django REST Framework
- Pandas
- Requests

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project_root
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---
---

## File Descriptions

1. **`models.py`**
   - Defines the `GasStationRoute` model to store start and end coordinates, total cost, and fuel stops.

2. **`serializers.py`**
   - Serializes and deserializes data for the `GasStationRoute` model.

3. **`views.py`**
   - Contains the core logic for route calculation, fuel optimization, and cost calculation.

4. **`fuel-prices-with-coordinates.csv`**
   - CSV file containing fuel prices and coordinates for gas stations.

5. **`requirements.txt`**
   - Lists all dependencies for the project.

---

## Key Functions

### In `models.py`
- `find_cheapest_fuel_station`: Finds the cheapest gas station within a given distance.
- `fill_gas`: Handles refueling and updates the total cost.
- `fetch_route`: Fetches the route using OSRM API.
  
---

## Author
[Sami Talebian]

