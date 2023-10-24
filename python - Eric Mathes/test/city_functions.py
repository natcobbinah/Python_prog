def city_country(city_name, country, population = ''):
    """Set city name and country together"""
    if population:
        output =  f"{city_name}, {country} - population {population}"
    else:
       output = f"{city_name}, {country}"
    return output