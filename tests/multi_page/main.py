from app import FletMVCApplication
from module import FletMVCModule
from multi_page.controller import CountriesController
from multi_page.model import CountriesModel
from multi_page.view import CountriesListView, CountryDetailView


app = FletMVCApplication("Countries MVC Application")

countries_list = FletMVCModule(model_class=CountriesModel,
                               view_class=CountriesListView,
                               controller_class=CountriesController)

country_detail = FletMVCModule(model_class=CountriesModel,
                               view_class=CountryDetailView,
                               controller_class=CountriesController)

app.add_route("/", countries_list)
app.add_route("/country/:country_name", country_detail)

app.run()
