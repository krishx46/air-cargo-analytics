import random
from datetime import datetime, timedelta
from faker import Faker
from pathlib import Path

import pandas as pd
import numpy as np
from reference_data import AIRPORTS, AIRCRAFT_MODELS, CUSTOMER_TYPES,  COMPANY_MASTER, EMIRATES_DESTINATIONS, WEATHER_BY_REGION, CARGO_PROPERTIES, INDUSTRY_CARGO
import math

fake = Faker()

random.seed(42)
np.random.seed(42)
Faker.seed(42)


# ============================
# OUTPUT FILES
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw"
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

# =========================
# AIRPORT LOOKUP
# =========================

AIRPORT_LOOKUP = {}
for airport in AIRPORTS:
    country = airport['country']
    if country not in AIRPORT_LOOKUP:
        AIRPORT_LOOKUP[country] = []
        
    AIRPORT_LOOKUP[country].append(airport)

# ======================================
# AIRPORT CODE LOOKUP
# ======================================
AIRPORT_CODE_LOOKUP = {
    airport["airport_code"]:airport for airport in AIRPORTS
}

# ========================
# CONFIGURATION
# ==========================


NUM_AIRPORTS = 40
NUM_AIRCRAFTS = 100
NUM_CUSTOMERS = 2500
NUM_FLIGHTS = 8000
NUM_SHIPMENTS = 75000
NUM_WEATHER_RECORDS = 14600
# ==========================
# HAVERSINE FORMULA FOR DISTANCE CALCULATION
# ==========================
def calculate_distance(origin, destination):

    R = 6371

    lat1 = math.radians(origin["latitude"])
    lon1 = math.radians(origin["longitude"])

    lat2 = math.radians(destination["latitude"])
    lon2 = math.radians(destination["longitude"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(R * c)



def generate_airports():
    airport_df = pd.DataFrame(AIRPORTS)
    output_file = RAW_DATA_PATH/"airports.csv"
    airport_df.to_csv(output_file, index=False)
    print(f"Generated {len(airport_df)} airports and saved to {output_file}")


def generate_aircraft():

    aircraft = []

    for aircraft_id in range(1, NUM_AIRCRAFTS + 1):

        model = random.choices(AIRCRAFT_MODELS,
                               weights=[40, 15, 10, 10, 5, 5, 10, 5], k=1)[0]

        aircraft.append({
            "aircraft_id": aircraft_id,
            "aircraft_type": model["aircraft_type"],
            "manufacturer": model["manufacturer"],
            "capacity_kg": model["capacity_kg"],
            "range_km": model["range_km"],
            "manufacture_year": random.randint(2005, 2025),
            "aircraft_status": random.choices(
                ["Active", "Maintenance", "Retired"],
                weights=[85, 10, 5],
                k=1
            )[0]
        })

    aircraft_df = pd.DataFrame(aircraft)

    output_file = RAW_DATA_PATH / "aircraft.csv"

    aircraft_df.to_csv(output_file, index=False)

    print(f"Generated aircraft.csv ({len(aircraft_df)} rows)")
    

def generate_customers():
    customers = []
    for customer_id in range(1, NUM_CUSTOMERS + 1):
        company = random.choice(COMPANY_MASTER)
        airport = random.choice(AIRPORT_LOOKUP[company["country"]])
        domain = (company["company"].lower().replace(" " ,"").replace("&", "and").replace(".", ""))
        email = f"contact{customer_id}@{domain}.com"

        customers.append({
            "customer_id": customer_id,
            "customer_name": f"{company['company']}-{airport['city']}",
            "customer_type": random.choice(CUSTOMER_TYPES),
            "industry": company["industry"],
            "country": airport["country"],
            "city": airport["city"],
            "email": email,
            "phone": fake.numerify("+###########")
        })
    customers_df = pd.DataFrame(customers)
    output_file = RAW_DATA_PATH / "customers.csv"
    customers_df.to_csv(output_file, index=False)
    print(f"Generated customers.csv ({len(customers_df)} rows)")

# =========================
# DATE
# =========================


START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)


def generate_departure_time():

    total_days = (END_DATE - START_DATE).days

    departure = START_DATE + timedelta(
        days=random.randint(0, total_days),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    return departure


def calculate_arrival_time(departure_time, distance_km):

    average_speed = 850

    flight_hours = distance_km / average_speed

    turnaround = random.randint(20, 60)/60

    total_time = flight_hours + turnaround

    return departure_time + timedelta(hours=total_time)


def generate_flight_status():

    return random.choices(
        [
            "On Time",
            "Delayed",
            "Landed",
            "Scheduled",
            "Cancelled"
        ],
        weights=[70, 15, 10, 4, 1],
        k=1
    )[0]


def generate_flights():
    flights = []
    for flight_id in range(1, NUM_FLIGHTS + 1):
        flight_number = f"EK{1000 + flight_id}"
        if random.random() < 0.6:
            origin = AIRPORT_CODE_LOOKUP["DXB"]
            destination_code = random.choice(EMIRATES_DESTINATIONS)
            destination = AIRPORT_CODE_LOOKUP[destination_code]
        else:
            destination = AIRPORT_CODE_LOOKUP["DXB"]
            origin_code = random.choice(EMIRATES_DESTINATIONS)
            origin = AIRPORT_CODE_LOOKUP[origin_code]
        distance = round(calculate_distance(origin, destination))
        aircraft_id = random.randint(1, NUM_AIRCRAFTS)
        departure_time = generate_departure_time()
        arrival_time = calculate_arrival_time(departure_time, distance).replace(microsecond=0)
        flight_status = generate_flight_status()
        flights.append({
            "flight_number": flight_number,
            "origin_airport": origin['airport_code'],
            "destination_airport": destination['airport_code'],
            "aircraft_id": aircraft_id,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "distance_km": distance,
            "flight_status": flight_status
        })
    flights_df = pd.DataFrame(flights)
    output_file = RAW_DATA_PATH / "flights.csv"
    flights_df.to_csv(output_file, index=False)
    print(f"Generated flights.csv ({len(flights_df)} rows)")

# ========================
# WEATHER RISK
# ========================
def get_delay_risk(weather):

    if weather in ["Sunny", "Clear", "Hot"]:
        return "Low"

    elif weather in ["Cloudy", "Rain"]:
        return "Medium"

    else:
        return "High"
    
def generate_temperature(region):

    if region == "Middle East":
        return round(random.uniform(25,48),1)

    elif region == "Europe":
        return round(random.uniform(-5,30),1)

    elif region == "Asia":
        return round(random.uniform(10,35),1)

    elif region == "North America":
        return round(random.uniform(-10,32),1)

    elif region == "Africa":
        return round(random.uniform(18,42),1)

    else:
        return round(random.uniform(8,30),1)


def generate_visibility(weather):

    if weather in ["Sunny","Clear","Hot"]:
        return round(random.uniform(8,10),1)

    elif weather == "Cloudy":
        return round(random.uniform(5,8),1)

    elif weather == "Rain":
        return round(random.uniform(2,6),1)

    elif weather == "Fog":
        return round(random.uniform(0.2,2),1)

    elif weather == "Snow":
        return round(random.uniform(0.5,3),1)

    else:
        return round(random.uniform(1,5),1)
    
def generate_wind(weather):

    if weather in ["Sunny","Clear","Hot"]:
        return random.randint(5,20)

    elif weather == "Cloudy":
        return random.randint(10,30)

    elif weather == "Rain":
        return random.randint(20,40)

    elif weather == "Fog":
        return random.randint(5,20)

    elif weather == "Snow":
        return random.randint(20,50)

    else:
        return random.randint(30,70)

 
 
def generate_weather():
    weather = []
    weather_id = 1
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    for airport in AIRPORTS:
        region = airport['region']
        current_date = start_date
        while current_date <= end_date:
            condition = random.choice(WEATHER_BY_REGION[region]) 
            temperature = generate_temperature(region)
            visibility = generate_visibility(condition)
            wind = generate_wind(condition)
            delay = get_delay_risk(condition)
            
            weather.append({
                "weather_id": weather_id,
                "airport_code": airport["airport_code"],
                "weather_date": current_date.date(),
                "weather_condition": condition,
                "temperature_c": temperature,
                "visibility_km": visibility,
                "wind_speed_kmh": wind,
                "delay_risk": delay
            })
            weather_id += 1
            current_date += timedelta(days=1)  
            
    weather_df = pd.DataFrame(weather)
    weather_df.to_csv(RAW_DATA_PATH/"weather.csv", index=False)
    print(f"Generated Weather csv ({len(weather_df)} rows)")
    

def get_cargo_details(industry):
    cargo = random.choice(INDUSTRY_CARGO[industry])
    properties = CARGO_PROPERTIES[cargo]
    return cargo, properties


def generate_shipment():
    customer_df = pd.read_csv(RAW_DATA_PATH/"customers.csv")
    flights_df = pd.read_csv(RAW_DATA_PATH/"flights.csv")
    weather_df = pd.read_csv(RAW_DATA_PATH/"weather.csv")
    weather_df["weather_date"] = pd.to_datetime(
    weather_df["weather_date"]).dt.date
    weather_lookup = {}
    for _, row in weather_df.iterrows():

        weather_lookup[
    
            (
                row["airport_code"],
                row["weather_date"])] = row["delay_risk"]
    
    shipment=[]
    for shipment_id in range(1, NUM_SHIPMENTS+1):
        #shipment
        
        customer = customer_df.sample(1).iloc[0]
        cargo_type, cargo = get_cargo_details(customer["industry"])
        weight = round(random.uniform(*cargo['weight']), 2)
        volume = round(weight / 160, 2)
        rate = round(random.uniform(*cargo['rate']), 2)
        revenue = round(weight*rate, 2)
        priority = cargo['priority']
        # flights
        
        flight = flights_df.sample(1).iloc[0]
        flight_number = flight["flight_number"]
        origin_airport = flight["origin_airport"]
        departure_time = pd.to_datetime(flight["departure_time"])
        delay_risk = weather_lookup[(origin_airport, departure_time.date())]
        # SHIPMENT STATUS
        if delay_risk == "Low":
            shipment_status = random.choices(
                ['Delivered', 'In Transit'],
                weights=[90,10],
                k=1
            )[0]
        elif delay_risk == "Medium":
            shipment_status = random.choices(
                ["Delivered", "Delayed", "In Transit"],
                weights=[60,25,15],
                k=1
            )[0]
        else:
            shipment_status = random.choices(
                ["Delivered", "Delayed", "Cancelled"],
                weights=[60,25,15],
                k=1
            )[0]
        shipment_date = departure_time.date()
        if shipment_status == "Delivered":
            delivery_date = shipment_date + timedelta(
                days=random.randint(1,4)
            )
        elif shipment_status == "Delayed":
            delivery_date = shipment_date + timedelta(
                days=random.randint(4,8)
                
            )
        elif shipment_status == "In Transit":
            delivery_date = shipment_date + timedelta(
                days=random.randint(2,6)
            )
        else:
            delivery_date = shipment_date
        
        shipment.append({

            "shipment_id": shipment_id,

            "customer_id": customer["customer_id"],

            "flight_number": flight_number,

            "shipment_date": shipment_date,

            "delivery_date": delivery_date,

            "cargo_type": cargo_type,

            "weight_kg": weight,

            "volume_cbm": volume,

            "revenue_usd": revenue,

            "shipment_status": shipment_status,

            "priority_level": priority
    })
    shipment_df = pd.DataFrame(shipment)
    output_file = RAW_DATA_PATH / "shipment.csv"
    shipment_df.to_csv(output_file, index=False)
    print(f"Generated shipment csv({len(shipment_df)} rows)")
    
            
        
        

def main():
    print("=" * 50)
    print("Enterprise Air Cargo Analytics Platform")
    print("=" * 50)

    print("\nGenerating Airports...")
    generate_airports()   
    print("\nGenerating Aircraft...")
    generate_aircraft()
    print("\nGenerating Customers...")
    generate_customers()
    print("\nGeneration Complete!")
    print("\nGenerating Flights...")
    generate_flights()
    print("\nGenerating Weather Report")
    generate_weather()
    print("\nGenerating shipment Report")
    generate_shipment()

if __name__ == "__main__":
    main()