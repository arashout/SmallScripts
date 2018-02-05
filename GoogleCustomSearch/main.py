from typing import List
import os
import pprint

from google import google

# TODO: Maybe don't hard-code in the future

MAX_COUNT = 3

def yieldSearchTerms() -> List[str]:
    universities = [
        "Dalhousie Clinical Psych PhD",
        "Lakehead Clinical Psych PhD",
        "Laval Clinical Psych PhD",
        "McGill Clinical Psych PhD",
        "McGill Counselling Psych PhD",
        "Queens University Clinical Psych PhD",
        "Simon Fraser University Clinical Psych PhD",
        "University of Alberta Clinical Psych PhD",
        "University of British Columbia Clinical Psych PhD",
        "University of British Columbia Counselling Psych PhD",
        "University of Calgary Clinical Psych PhD",
        "University of Concordia Clinical Psych PhD",
        "University of Guelph Clinical Psych PhD",
        "University of Manitoba Clinical Psych PhD",
        "University of Montreal Clinical Psych PhD",
        "University of Montreal Clinical Psych PsyD",
        "University of New Brunswick Clinical Psych PhD",
        "University of Ottawa Clinical Psych PhD",
        "University of Regina Clinical Psych PhD",
        "University of Saskatchewan Clinical Psych PhD",
        "University of Toronto Clinical and Counselling Psych PhD",
        "University of Toronto School and Clinical Child Psych PhD",
        "University of Victoria Clinical Psych PhD",
        "University of Waterloo Clinical Psych PhD",
        "University of Western Ontario Clinical Psych PhD",
        "University of Windsor Clinical Psych PhD",
        "York University Clinical Psych PhD",
        "York University Clinical Developmental Psych PhD",
        "Universite de Sherbrooke PhD Clinical Psych",
        "Universite de Sherbrooke PhD clinical intervention with children and adolescents",
        "McMaster PhD Psychology, Neuroscience & Behaviour"
    ]
    for uni in universities:
        search_query = "'{0}' '{1}' '{2}'".format(uni, 'fund*', 'guarantee*')
        yield search_query


def main():
    developer_key = os.environ.get('CUSTOM_SEARCH_API_KEY')
    search_engine_id = os.environ.get('CUSTOM_SEARCH_SEARCH_ENGINE_ID')
    if developer_key is None or search_engine_id is None:
        print('Missing credentials')
        exit()

    for query in yieldSearchTerms():
        results = google.search(query)

        for i, result in enumerate(results):
            title = result.name.replace('\n', ' ')
            description = result.description.replace('\n', ' ')
            print(' "{0}" ,{1},"{2}","{3}"'.format(query, result.google_link , title, description))
            
            if i > MAX_COUNT:
                break


if __name__ == '__main__':
    main()
