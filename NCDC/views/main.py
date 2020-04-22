from requests import get
from bs4 import BeautifulSoup
from NCDC.views.coordinates import get_co_ordinates

SITE_URL = 'https://covid19.ncdc.gov.ng'
site_data_format = ["state", "No_of_cases", "No_of_active_case", "No_discharged", "No_of_deaths"]


class ResponseData:
    def __init__(self, **kwargs):
        self.state = kwargs.get('state')
        self.No_of_cases = kwargs.get('No_of_cases')
        self.No_of_active_case = kwargs.get('No_of_active_case')
        self.No_discharged = kwargs.get('No_discharged')
        self.No_of_deaths = kwargs.get('No_of_deaths')
        self.coordinate = None

    def __str__(self):
        return f'{self.state} - {self.No_of_cases} cases'


def get_child_data(child_element):
    state_data = dict()
    for title, child in zip(site_data_format, child_element):
        state_data[title] = child.p.string
    return state_data


def scrap_ncdc_website():
    response = get(SITE_URL)
    soup = BeautifulSoup(response.content, "lxml")
    table = soup.find("table", id="custom3")
    table_rows = table.tbody.select("tr")
    all_state_data = list()

    for i, val in enumerate(table_rows):
        # skip the ist and last row
        if i == 0 or i + 1 == len(table_rows):
            continue
        data = ResponseData(**get_child_data(val.select("td")))
        data.coordinate = get_co_ordinates(data.state)
        all_state_data.append(data)
    return all_state_data


# if __name__ == "__main__":
#     results = scrap_ncdc_website()
#     for item in results:
#         print(item)

