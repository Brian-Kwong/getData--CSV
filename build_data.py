import county_demographics
from typing import List, Dict

class CountyDemographics:
    def __init__(self,
                  age: Dict[str,float],
                  county: str,
                  education: Dict[str,float],
                  ethnicities: Dict[str,float],
                  income: Dict[str,float],
                  population: Dict[str,float],
                  state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state
    def __repr__(self):
        return 'CountyDemographics({}, {}, {}, {}, {}, {}, {})'.format(
                    self.age,
                self.county,
                self.education,
                self.ethnicities,
                self.income,
                self.population,
                self.state
            )


def convert_county(county) -> CountyDemographics:
    if 'Median Houseold Income' in county['Income']:
        county['Income']['Median Household Income'] =\
                county['Income']['Median Houseold Income']
        del county['Income']['Median Houseold Income']
    return CountyDemographics(
            county['Age'],
            county['County'],
            county['Education'],
            county['Ethnicities'],
            county['Income'],
            county['Population'],
            county['State']
        )

def getData() -> List[CountyDemographics]:
    report = county_demographics.get_report()
    return [convert_county(county) for county in report]





