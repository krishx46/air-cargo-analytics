#===========================
# REFERENCE DATA
#===========================
AIRPORTS = [
    # Middle East
    {
        "airport_code": "DXB",
        "airport_name": "Dubai International Airport",
        "city": "Dubai",
        "country": "United Arab Emirates",
        "region": "Middle East",
        "latitude": 25.2532,
        "longitude": 55.3657
    },
    {
        "airport_code": "DWC",
        "airport_name": "Al Maktoum International Airport",
        "city": "Dubai",
        "country": "United Arab Emirates",
        "region": "Middle East",
        "latitude": 24.8964,
        "longitude": 55.1614
    },
    {
        "airport_code": "DOH",
        "airport_name": "Hamad International Airport",
        "city": "Doha",
        "country": "Qatar",
        "region": "Middle East",
        "latitude": 25.2731,
        "longitude": 51.6081
    },
    {
        "airport_code": "AUH",
        "airport_name": "Abu Dhabi International Airport",
        "city": "Abu Dhabi",
        "country": "United Arab Emirates",
        "region": "Middle East",
        "latitude": 24.4330,
        "longitude": 54.6511
    },
    {
        "airport_code": "RUH",
        "airport_name": "King Khalid International Airport",
        "city": "Riyadh",
        "country": "Saudi Arabia",
        "region": "Middle East",
        "latitude": 24.9576,
        "longitude": 46.6988
    },

    # Europe
    {
        "airport_code": "FRA",
        "airport_name": "Frankfurt Airport",
        "city": "Frankfurt",
        "country": "Germany",
        "region": "Europe",
        "latitude": 50.0379,
        "longitude": 8.5622
    },
    {
        "airport_code": "AMS",
        "airport_name": "Amsterdam Schiphol Airport",
        "city": "Amsterdam",
        "country": "Netherlands",
        "region": "Europe",
        "latitude": 52.3105,
        "longitude": 4.7683
    },
    {
        "airport_code": "LHR",
        "airport_name": "London Heathrow Airport",
        "city": "London",
        "country": "United Kingdom",
        "region": "Europe",
        "latitude": 51.4700,
        "longitude": -0.4543
    },
    {
        "airport_code": "CDG",
        "airport_name": "Charles de Gaulle Airport",
        "city": "Paris",
        "country": "France",
        "region": "Europe",
        "latitude": 49.0097,
        "longitude": 2.5479
    },
    {
        "airport_code": "LGG",
        "airport_name": "Liège Airport",
        "city": "Liège",
        "country": "Belgium",
        "region": "Europe",
        "latitude": 50.6374,
        "longitude": 5.4432
    },

    # Asia
    {
        "airport_code": "HKG",
        "airport_name": "Hong Kong International Airport",
        "city": "Hong Kong",
        "country": "China",
        "region": "Asia",
        "latitude": 22.3080,
        "longitude": 113.9185
    },
    {
        "airport_code": "SIN",
        "airport_name": "Singapore Changi Airport",
        "city": "Singapore",
        "country": "Singapore",
        "region": "Asia",
        "latitude": 1.3644,
        "longitude": 103.9915
    },
    {
        "airport_code": "PVG",
        "airport_name": "Shanghai Pudong International Airport",
        "city": "Shanghai",
        "country": "China",
        "region": "Asia",
        "latitude": 31.1443,
        "longitude": 121.8083
    },
    {
        "airport_code": "ICN",
        "airport_name": "Incheon International Airport",
        "city": "Seoul",
        "country": "South Korea",
        "region": "Asia",
        "latitude": 37.4602,
        "longitude": 126.4407
    },
    {
        "airport_code": "NRT",
        "airport_name": "Narita International Airport",
        "city": "Tokyo",
        "country": "Japan",
        "region": "Asia",
        "latitude": 35.7720,
        "longitude": 140.3929
    },

    # India
    {
        "airport_code": "DEL",
        "airport_name": "Indira Gandhi International Airport",
        "city": "Delhi",
        "country": "India",
        "region": "Asia",
        "latitude": 28.5562,
        "longitude": 77.1000
    },
    {
        "airport_code": "BOM",
        "airport_name": "Chhatrapati Shivaji Maharaj International Airport",
        "city": "Mumbai",
        "country": "India",
        "region": "Asia",
        "latitude": 19.0896,
        "longitude": 72.8656
    },
    {
        "airport_code": "BLR",
        "airport_name": "Kempegowda International Airport",
        "city": "Bengaluru",
        "country": "India",
        "region": "Asia",
        "latitude": 13.1986,
        "longitude": 77.7066
    },
    {
        "airport_code": "HYD",
        "airport_name": "Rajiv Gandhi International Airport",
        "city": "Hyderabad",
        "country": "India",
        "region": "Asia",
        "latitude": 17.2403,
        "longitude": 78.4294
    },
    {
        "airport_code": "MAA",
        "airport_name": "Chennai International Airport",
        "city": "Chennai",
        "country": "India",
        "region": "Asia",
        "latitude": 12.9941,
        "longitude": 80.1709
    },

    # North America
    {
        "airport_code": "JFK",
        "airport_name": "John F. Kennedy International Airport",
        "city": "New York",
        "country": "United States",
        "region": "North America",
        "latitude": 40.6413,
        "longitude": -73.7781
    },
    {
        "airport_code": "ORD",
        "airport_name": "O'Hare International Airport",
        "city": "Chicago",
        "country": "United States",
        "region": "North America",
        "latitude": 41.9742,
        "longitude": -87.9073
    },
    {
        "airport_code": "LAX",
        "airport_name": "Los Angeles International Airport",
        "city": "Los Angeles",
        "country": "United States",
        "region": "North America",
        "latitude": 33.9416,
        "longitude": -118.4085
    },
    {
        "airport_code": "DFW",
        "airport_name": "Dallas/Fort Worth International Airport",
        "city": "Dallas",
        "country": "United States",
        "region": "North America",
        "latitude": 32.8998,
        "longitude": -97.0403
    },
    {
        "airport_code": "MEM",
        "airport_name": "Memphis International Airport",
        "city": "Memphis",
        "country": "United States",
        "region": "North America",
        "latitude": 35.0425,
        "longitude": -89.9767
    },

    # Africa
    {
        "airport_code": "CAI",
        "airport_name": "Cairo International Airport",
        "city": "Cairo",
        "country": "Egypt",
        "region": "Africa",
        "latitude": 30.1219,
        "longitude": 31.4056
    },
    {
        "airport_code": "JNB",
        "airport_name": "O.R. Tambo International Airport",
        "city": "Johannesburg",
        "country": "South Africa",
        "region": "Africa",
        "latitude": -26.1337,
        "longitude": 28.2420
    },
    {
        "airport_code": "NBO",
        "airport_name": "Jomo Kenyatta International Airport",
        "city": "Nairobi",
        "country": "Kenya",
        "region": "Africa",
        "latitude": -1.3192,
        "longitude": 36.9278
    },

    # Oceania
    {
        "airport_code": "SYD",
        "airport_name": "Sydney Kingsford Smith Airport",
        "city": "Sydney",
        "country": "Australia",
        "region": "Oceania",
        "latitude": -33.9399,
        "longitude": 151.1753
    },
    {
        "airport_code": "MEL",
        "airport_name": "Melbourne Airport",
        "city": "Melbourne",
        "country": "Australia",
        "region": "Oceania",
        "latitude": -37.6690,
        "longitude": 144.8410
    },
    {
        "airport_code": "ZRH",
        "airport_name": "Zurich Airport",
        "city": "Zurich",
        "country": "Switzerland",
        "region": "Europe",
        "latitude": 47.4581,
        "longitude": 8.5555
    },
    {
        "airport_code": "CPH",
        "airport_name": "Copenhagen Airport",
        "city": "Copenhagen",
        "country": "Denmark",
        "region": "Europe",
        "latitude": 55.6181,
        "longitude": 12.6561
    },
    {
        "airport_code": "ARN",
        "airport_name": "Stockholm Arlanda Airport",
        "city": "Stockholm",
        "country": "Sweden",
        "region": "Europe",
        "latitude": 59.6519,
        "longitude": 17.9186
    },
    {
    "airport_code": "KWI",
    "airport_name": "Kuwait International Airport",
    "city": "Kuwait City",
    "country": "Kuwait",
    "region": "Middle East",
    "latitude": 29.2266,
    "longitude": 47.9689
},
{
    "airport_code": "BAH",
    "airport_name": "Bahrain International Airport",
    "city": "Manama",
    "country": "Bahrain",
    "region": "Middle East",
    "latitude": 26.2708,
    "longitude": 50.6336
},
{
    "airport_code": "MCT",
    "airport_name": "Muscat International Airport",
    "city": "Muscat",
    "country": "Oman",
    "region": "Middle East",
    "latitude": 23.5933,
    "longitude": 58.2844
},
{
    "airport_code": "AMM",
    "airport_name": "Queen Alia International Airport",
    "city": "Amman",
    "country": "Jordan",
    "region": "Middle East",
    "latitude": 31.7226,
    "longitude": 35.9932
},
{
    "airport_code": "PEK",
    "airport_name": "Beijing Capital International Airport",
    "city": "Beijing",
    "country": "China",
    "region": "Asia",
    "latitude": 40.0799,
    "longitude": 116.6031
},
{
    "airport_code": "MXP",
    "airport_name": "Milan Malpensa Airport",
    "city": "Milan",
    "country": "Italy",
    "region": "Europe",
    "latitude": 45.6306,
    "longitude": 8.7281
},
{
    "airport_code": "YYZ",
    "airport_name": "Toronto Pearson International Airport",
    "city": "Toronto",
    "country": "Canada",
    "region": "North America",
    "latitude": 43.6777,
    "longitude": -79.6248
}
]

# ============================
# AIRCRAFTS
# ===========================

AIRCRAFT_MODELS = [
    {
        "aircraft_type": "Boeing 777F",
        "manufacturer": "Boeing",
        "capacity_kg": 102000,
        "range_km": 9070
    },
    {
        "aircraft_type": "Boeing 747-8F",
        "manufacturer": "Boeing",
        "capacity_kg": 137000,
        "range_km": 8130
    },
    {
        "aircraft_type": "Boeing 767-300F",
        "manufacturer": "Boeing",
        "capacity_kg": 52000,
        "range_km": 6025
    },
    {
        "aircraft_type": "Airbus A330-200F",
        "manufacturer": "Airbus",
        "capacity_kg": 70000,
        "range_km": 7400
    },
    {
        "aircraft_type": "Airbus A350F",
        "manufacturer": "Airbus",
        "capacity_kg": 109000,
        "range_km": 8700
    },
    {
        "aircraft_type": "Antonov An-124",
        "manufacturer": "Antonov",
        "capacity_kg": 150000,
        "range_km": 4800
    },
    {
        "aircraft_type": "Boeing 737-800BCF",
        "manufacturer": "Boeing",
        "capacity_kg": 23500,
        "range_km": 3750
    },
    {
        "aircraft_type": "Airbus A321P2F",
        "manufacturer": "Airbus",
        "capacity_kg": 27000,
        "range_km": 4300
    }
]


# ===========================
# CUSTOMER TYPES
# ==========================
CUSTOMER_TYPES = [
    "Corporate",
    "SME",
    "Enterprise"
]


COMPANY_MASTER = [

# =========================
# Electronics
# =========================

{"company": "Samsung Electronics", "industry": "Electronics", "country": "South Korea"},
{"company": "LG Electronics", "industry": "Electronics", "country": "South Korea"},
{"company": "Sony", "industry": "Electronics", "country": "Japan"},
{"company": "Panasonic", "industry": "Electronics", "country": "Japan"},
{"company": "Canon", "industry": "Electronics", "country": "Japan"},
{"company": "Nikon", "industry": "Electronics", "country": "Japan"},
{"company": "Apple", "industry": "Electronics", "country": "United States"},
{"company": "Dell Technologies", "industry": "Electronics", "country": "United States"},
{"company": "HP Inc.", "industry": "Electronics", "country": "United States"},
{"company": "Intel", "industry": "Electronics", "country": "United States"},
{"company": "NVIDIA", "industry": "Electronics", "country": "United States"},
{"company": "Cisco", "industry": "Electronics", "country": "United States"},
{"company": "Huawei", "industry": "Electronics", "country": "China"},
{"company": "Lenovo", "industry": "Electronics", "country": "China"},
{"company": "Xiaomi", "industry": "Electronics", "country": "China"},
# =========================
# Logistics
# =========================

{"company": "DHL", "industry": "Logistics", "country": "Germany"},
{"company": "FedEx", "industry": "Logistics", "country": "United States"},
{"company": "UPS", "industry": "Logistics", "country": "United States"},
{"company": "DB Schenker", "industry": "Logistics", "country": "Germany"},
{"company": "Kuehne + Nagel", "industry": "Logistics", "country": "Switzerland"},
{"company": "DSV", "industry": "Logistics", "country": "Denmark"},
{"company": "Maersk Logistics", "industry": "Logistics", "country": "Denmark"},
{"company": "Nippon Express", "industry": "Logistics", "country": "Japan"},
{"company": "Expeditors", "industry": "Logistics", "country": "United States"},
{"company": "Sinotrans", "industry": "Logistics", "country": "China"},
# =========================
# Automotive
# =========================

{"company": "Toyota", "industry": "Automotive", "country": "Japan"},
{"company": "Honda", "industry": "Automotive", "country": "Japan"},
{"company": "Nissan", "industry": "Automotive", "country": "Japan"},
{"company": "BMW", "industry": "Automotive", "country": "Germany"},
{"company": "Mercedes-Benz", "industry": "Automotive", "country": "Germany"},
{"company": "Volkswagen", "industry": "Automotive", "country": "Germany"},
{"company": "Audi", "industry": "Automotive", "country": "Germany"},
{"company": "Hyundai", "industry": "Automotive", "country": "South Korea"},
{"company": "Kia", "industry": "Automotive", "country": "South Korea"},
{"company": "Tesla", "industry": "Automotive", "country": "United States"},
{"company": "Ford", "industry": "Automotive", "country": "United States"},
{"company": "General Motors", "industry": "Automotive", "country": "United States"},
{"company": "Tata Motors", "industry": "Automotive", "country": "India"},
{"company": "Mahindra", "industry": "Automotive", "country": "India"},
# =========================
# Retail
# =========================

{"company": "Amazon", "industry": "Retail", "country": "United States"},
{"company": "Walmart", "industry": "Retail", "country": "United States"},
{"company": "Costco", "industry": "Retail", "country": "United States"},
{"company": "Target", "industry": "Retail", "country": "United States"},
{"company": "Carrefour", "industry": "Retail", "country": "France"},
{"company": "IKEA", "industry": "Retail", "country": "Sweden"},
{"company": "Lulu Hypermarket", "industry": "Retail", "country": "United Arab Emirates"},
{"company": "Noon", "industry": "Retail", "country": "United Arab Emirates"},
{"company": "Reliance Retail", "industry": "Retail", "country": "India"},
{"company": "Alibaba", "industry": "Retail", "country": "China"},
# =========================
# Manufacturing
# =========================

{"company": "Siemens", "industry": "Manufacturing", "country": "Germany"},
{"company": "Bosch", "industry": "Manufacturing", "country": "Germany"},
{"company": "ABB", "industry": "Manufacturing", "country": "Switzerland"},
{"company": "Schneider Electric", "industry": "Manufacturing", "country": "France"},
{"company": "General Electric", "industry": "Manufacturing", "country": "United States"},
{"company": "3M", "industry": "Manufacturing", "country": "United States"},
{"company": "Honeywell", "industry": "Manufacturing", "country": "United States"},
{"company": "Mitsubishi Heavy Industries", "industry": "Manufacturing", "country": "Japan"},
{"company": "Hitachi", "industry": "Manufacturing", "country": "Japan"},
{"company": "Larsen & Toubro", "industry": "Manufacturing", "country": "India"},

]

# ===========================
# FLIGHT STATUS
# ==========================
FLIGHT_STATUS = [
    "Scheduled",
    "On Time",
    "Delayed",
    "Cancelled",
    "Landed"
]

EMIRATES_DESTINATIONS = [
    # Middle East
    "DOH", "RUH", "KWI", "BAH", "MCT", "AMM",

    # India
    "DEL", "BOM", "BLR", "HYD", "MAA",

    # Asia
    "SIN", "HKG", "ICN", "NRT", "PVG", "PEK",

    # Europe
    "LHR", "FRA", "CDG", "AMS", "ZRH", "MXP",

    # Africa
    "JNB", "NBO", "CAI",

    # North America
    "JFK", "ORD", "LAX", "YYZ",

    # Oceania
    "SYD", "MEL"
]
# ==========================
# WEATHER CONDITIONS BY REGION
# ==========================
WEATHER_BY_REGION = {

    "Middle East": [
        "Sunny",
        "Clear",
        "Hot",
        "Dust Storm"
    ],

    "Europe": [
        "Sunny",
        "Cloudy",
        "Rain",
        "Fog",
        "Snow"
    ],

    "Asia": [
        "Sunny",
        "Cloudy",
        "Rain",
        "Thunderstorm"
    ],

    "North America": [
        "Sunny",
        "Cloudy",
        "Rain",
        "Snow"
    ],

    "Africa": [
        "Sunny",
        "Hot",
        "Cloudy"
    ],

    "Oceania": [
        "Sunny",
        "Rain",
        "Cloudy"
    ]
}
# ====================
# CARGO TYPES BY INDUSTRY
# ====================


INDUSTRY_CARGO = {
    "Electronics": [
        "Consumer Electronics",
        "Semiconductors",
        "Computer Components",
        "Telecommunication Equipment"
    ],

    "Pharmaceuticals": [
        "Vaccines",
        "Medicines",
        "Medical Equipment",
        "Diagnostic Kits"
    ],

    "Automotive": [
        "Auto Parts",
        "Engine Components",
        "Transmission Parts",
        "Tyres"
    ],

    "Retail": [
        "Clothing",
        "Footwear",
        "Accessories",
        "Consumer Goods"
    ],

    "Food & Beverage": [
        "Fresh Produce",
        "Frozen Food",
        "Beverages",
        "Dairy Products"
    ],

    "Manufacturing": [
        "Industrial Machinery",
        "Machine Parts",
        "Raw Materials",
        "Industrial Equipment"
    ],
    "Logistics": [
        "General Cargo",
        "Courier Parcels",
        "Warehouse Equipment",
        "Packaging Materials"
    ]
}
# =================
# CARGO PROPORTIES
# =================
CARGO_PROPERTIES = {

    "Vaccines": {
        "weight": (50, 500),
        "rate": (12, 18),
        "priority": "Critical"
    },

    "Medicines": {
        "weight": (100, 1000),
        "rate": (8, 15),
        "priority": "High"
    },

    "Medical Equipment": {
        "weight": (200, 3000),
        "rate": (7, 12),
        "priority": "High"
    },

    "Semiconductors": {
        "weight": (20, 300),
        "rate": (20, 35),
        "priority": "High"
    },

    "Consumer Electronics": {
        "weight": (100, 2500),
        "rate": (6, 10),
        "priority": "Medium"
    },

    "Computer Components": {
        "weight": (50, 1000),
        "rate": (10, 18),
        "priority": "High"
    },

    "Auto Parts": {
        "weight": (500, 8000),
        "rate": (2, 5),
        "priority": "Medium"
    },

    "Industrial Machinery": {
        "weight": (1000, 15000),
        "rate": (1.5, 3),
        "priority": "Low"
    },

    "Fresh Produce": {
        "weight": (500, 5000),
        "rate": (2, 4),
        "priority": "High"
    },

    "Frozen Food": {
        "weight": (500, 4000),
        "rate": (2.5, 5),
        "priority": "High"
    },

    "Clothing": {
        "weight": (200, 3000),
        "rate": (3, 6),
        "priority": "Medium"
    },

    "Consumer Goods": {
        "weight": (300, 4000),
        "rate": (2, 5),
        "priority": "Medium"
    },
    "Tyres": {
        "weight": (300, 3000),
        "rate": (2, 5),
        "priority": "Medium"
    },
    "General Cargo": {
        "weight": (100, 5000),
        "rate": (2, 5),
        "priority": "Medium"
    },

    "Courier Parcels": {
        "weight": (1, 100),
        "rate": (8, 15),
        "priority": "High"
    },

    "Warehouse Equipment": {
        "weight": (500, 8000),
        "rate": (2, 4),
        "priority": "Medium"
    },

    "Packaging Materials": {
        "weight": (100, 3000),
        "rate": (1, 3),
        "priority": "Low"
    },
        "Telecommunication Equipment": {
        "weight": (100, 2000),
        "rate": (8, 15),
        "priority": "High"
    },

    "Diagnostic Kits": {
        "weight": (20, 500),
        "rate": (10, 18),
        "priority": "Critical"
    },

    "Engine Components": {
        "weight": (500, 5000),
        "rate": (2, 5),
        "priority": "Medium"
    },

    "Transmission Parts": {
        "weight": (400, 4000),
        "rate": (2, 5),
        "priority": "Medium"
    },

    "Footwear": {
        "weight": (100, 2000),
        "rate": (3, 6),
        "priority": "Medium"
    },

    "Accessories": {
        "weight": (50, 1000),
        "rate": (4, 8),
        "priority": "Medium"
    },

    "Beverages": {
        "weight": (500, 5000),
        "rate": (2, 4),
        "priority": "High"
    },

    "Dairy Products": {
        "weight": (300, 3000),
        "rate": (2, 5),
        "priority": "High"
    },

    "Machine Parts": {
        "weight": (500, 6000),
        "rate": (2, 4),
        "priority": "Medium"
    },

    "Raw Materials": {
        "weight": (1000, 12000),
        "rate": (1.5, 3),
        "priority": "Low"
    },

    "Industrial Equipment": {
        "weight": (800, 10000),
        "rate": (2, 4),
        "priority": "Medium"
    }
}