
def get_formatted_city(city, country, population=''):
    if population:
        full_naming = f"{city}, {country} - population {population}."
    else:    
        full_naming = f"{city}, {country}."
    return full_naming.title()
 