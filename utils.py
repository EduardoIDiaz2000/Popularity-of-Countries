def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict.get('2022 Population', '0').replace(',', '')),
    '2020': int(country_dict.get('2020 Population', '0').replace(',', '')),
    '2015': int(country_dict.get('2015 Population', '0').replace(',', '')),
    '2010': int(country_dict.get('2010 Population', '0').replace(',', '')),
    '2000': int(country_dict.get('2000 Population', '0').replace(',', '')),
    '1990': int(country_dict.get('1990 Population', '0').replace(',', '')),
    '1980': int(country_dict.get('1980 Population', '0').replace(',', '')),
    '1970': int(country_dict.get('1970 Population', '0').replace(',', '')),
  }
  return list(population_dict.keys()), list(population_dict.values())



def population_by_country(data, country):
  return list(filter(lambda item: item['Country'].strip().lower() == country.strip().lower(), data))
