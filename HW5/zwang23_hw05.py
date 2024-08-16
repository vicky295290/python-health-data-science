import requests

def get_data(name):
    """Function to get RxCUI data.

    Typical Usage Example:

    get_data('Aspirin')

    args:
        name: input drug name, string.

    returns:
        requested data for input drug name, list.

    """
    url = 'https://rxnav.nlm.nih.gov/REST/rxcui.json'
    parameters = {'name': name}

    #Make the HTTP GET request
    req = requests.get(url, params=parameters)

    #now, load the json data for our processing
    data = req.json()['idGroup']['rxnormId']
    # print('get_data output: \n',data)

    return data

def get_url(rxcui):
    """Function to get medication records with urls from medlineplus

    Typical Usage Example:

    get_url(rxcui)

    args:
        rxcui: input RxCUI data, list.

    returns:
        url for the input data, string.

    """
    url = 'https://connect.medlineplus.gov/service'
    parameters = {
        'mainSearchCriteria.v.cs': '2.16.840.1.113883.6.88',
        'mainSearchCriteria.v.c': rxcui,
        'knowledgeResponseType': 'application/json'
    }

    #Make the HTTP GET request
    req = requests.get(url, params=parameters)

    #now, load the json data for our processing
    data = req.json()['feed']['entry'][0]['link'][0]['href']

    return data

drug_names = ['Aspirin', 'Escitalopram', 'Metformin']

for i in drug_names:
    urls = get_url(get_data(i))
    cleaned_urls = urls.removesuffix('?utm_source=mplusconnect&utm_medium=service')
    print("{} - {}\r".format(i, cleaned_urls))
