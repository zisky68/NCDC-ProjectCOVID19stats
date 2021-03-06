CITIES = {
    "Rivers": (4.824167, 7.033611),
    "Borno": (11.833333, 13.150000),
    "Kano": (12.000000, 8.516667),
    "Katsina": (12.985531, 7.617144),
    "Anambra": (6.010519, 6.910345),
    "Cross River": (4.982873, 8.334503),
    "Delta": (5.879698, 5.700531),
    "Oyo": (7.536318, 3.418143),
    "Plateau": (9.896527, 8.858331),
    "Kaduna": (10.609319, 7.429504),
    "Niger": (9.583555, 6.546316),
    "Sokoto": (13.005873, 5.247552),
    "Adamawa": (9.203496, 12.495390),
    "Edo": (6.339185, 5.617447),
    "Ondo": (7.100005, 4.841694),
    "Enugu": (6.459964, 7.548949),
    "Imo": (5.476310, 7.025853),
    "Bauchi": (10.314159, 9.846282),
    "Ekiti": (7.621111, 5.221389),
    "Gombe": (10.283333, 11.166667),
    "Jigawa": (12.1, 9.56),
    "Ogun": (7.0, 3.58333),
    "Abia": (5.41667, 7.5),
    "Benue": (7.33333, 8.75),
    "Kwara": (8.500000, 4.550000),
    "Kebbi": (12.466078, 4.199524),
    "Akwa Ibom": (5.038963, 7.909470),
    "Abuja FCT": (9.072264, 7.491302),
    "Zamfara": (12.600000, 6.589722),
    "Lagos": (6.465422, 3.406448),
    "Awka": (6.210528, 7.072277),
    "Bayelsa": (4.75, 6.08333),
    "Ebonyi": (6.25, 8.08333),
    "Kogi": (4.75, 6.08333),
    "Nasarawa": (8.5, 8.25),
    "Taraba": (8.0, 10.5),
    "Yobe": (12.0, 11.5),
}


def get_co_ordinates(state_name):
    return CITIES.get(state_name)
