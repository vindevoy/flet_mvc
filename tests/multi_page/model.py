import pandas as pd
import plotly.express as px

from flet_mvc.model import FletMVCModel


class CountriesModel(FletMVCModel):
    _countries = []

    def __init__(self):
        super().__init__()

        self._countries: pd.DataFrame = px.data.gapminder()

    def get_continent_list(self) -> list:
        return self._countries["continent"].unique().tolist()

    def get_country_list(self) -> list:
        return self._countries["country"].unique().tolist()

    def get_country_list_for_continent(self, continent_name: str) -> list:
        countries = self._countries
        countries = countries[countries["continent"] == continent_name].copy()
        return countries["country"].unique().tolist()

    def __get_country_data(self, country_name: str):
        countries = self._countries
        countries = countries[countries["country"] == country_name].copy()
        countries["lifeExp"] = countries["lifeExp"].round(1)
        countries.drop(["country"], axis=1, inplace=True)

        return countries.to_dict("records")

    def get_country_life_expectancy(self, country_name: str):
        return [{key.replace("lifeExp", "life_expect"): data[key]
                 for key in ["year", "lifeExp"]}
                for data in self.__get_country_data(country_name)]

    def get_country_population(self, country_name: str):
        return [{key.replace("pop", "population"): data[key]
                 for key in ["year", "pop"]}
                for data in self.__get_country_data(country_name)]

    def get_country_gdp(self, country_name: str):
        data = [{key.replace("pop", "population").replace("gdpPercap", "gdp_per_cap"): data[key]
                 for key in ["year", "pop", "gdpPercap"]}
                for data in self.__get_country_data(country_name)]

        return [{**d, "gdp": d["gdp_per_cap"] * d["population"]} for d in data]  # add calculated column


def test_continents():
    m = CountriesModel()
    continents = m.get_continent_list()

    assert type(continents) is list  # check the type
    assert len(continents) == 5  # check the number of records
    assert type(continents[0]) is str  # check if this is a list of string


def test_countries():
    m = CountriesModel()
    countries = m.get_country_list()

    assert type(countries) is list  # check the type
    assert len(countries) == 142  # check the number of records
    assert type(countries[0]) is str  # check if this is a list of string

    countries = m.get_country_list_for_continent("Europe")

    assert type(countries) is list  # check the type
    assert len(countries) == 30  # check the number of records
    assert type(countries[0]) is str  # check if this is a list of string


def test_belgium():
    m = CountriesModel()
    bel = m.get_country_life_expectancy("Belgium")

    assert type(bel) is list
    assert len(bel) == 12

    b52 = bel[0]
    assert type(b52) is dict
    assert len(b52) == 2  # 2 key-value pairs
    assert "year" in b52
    assert "life_expect" in b52
    assert b52["year"] == 1952

    bel = m.get_country_population("Belgium")

    assert type(bel) is list
    assert len(bel) == 12

    b52 = bel[0]
    assert type(b52) is dict
    assert len(b52) == 2  # 2 key-value pairs
    assert "year" in b52
    assert "population" in b52
    assert b52["year"] == 1952

    bel = m.get_country_gdp("Belgium")

    assert type(bel) is list
    assert len(bel) == 12

    b52 = bel[0]
    assert type(b52) is dict
    assert len(b52) == 4  # 4 key-value pairs this time
    assert "year" in b52
    assert "population" in b52
    assert "gdp_per_cap" in b52
    assert "gdp" in b52
    assert b52["year"] == 1952


if __name__ == "__main__":
    test_continents()
    test_countries()
    test_belgium()
