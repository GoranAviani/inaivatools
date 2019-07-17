#Check do we have support for the api country code
def check_country_code(telCountry):
    
    if telCountry in ["SE", "FI", "YU"]:
        return "existing_country"
    else:
        return "non_existing_country"