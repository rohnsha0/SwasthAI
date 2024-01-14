import requests
from bs4 import BeautifulSoup


def getDoctorGeneralMedApollo(
        city: str = 'kolkata'
):
    appollo_webpage = requests.get(
        f'https://www.askapollo.com/physical-appointment/city/{city}?speciality=General%20Physician&page=1').text
    appollo_soup = BeautifulSoup(appollo_webpage, 'lxml')
    doctor_details = appollo_soup.find_all('div', class_='dr-list')
    doctor_names = []
    for i in doctor_details:
        doctor_names.append(i.find_all('h3')[0].text.strip())
    spec_grp = appollo_soup.find_all('div', class_='spec-group')
    doctor_spec = []
    for i in spec_grp:
        doctor_spec.append(i.text.strip().split('|'))
    doctors_data = {}
    for i in range(len(doctor_names)):
        doctor_data = [doctor_names[i], doctor_spec[i][0], doctor_spec[i][1]]

        category = 'physical'
        if category not in doctors_data:
            doctors_data[category] = []

        doctors_data[category].append(doctor_data)
    return doctors_data


def getDoctorGeneralMedPracto(
        city='kolkata'
):
    practo_webpage = requests.get(
        f'https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22General%20Physician%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city={city}'
    ).text
