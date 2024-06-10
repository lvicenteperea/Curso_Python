import argparse
import urllib.parse
import json
import os
from typing import Any, Dict, List
from vantablack import utilities

def email_ids_to_file(directory: str, data: Any) -> None:
    #creating the file with email ids
    filename = "emails_ids.json"
    path = os.path.join(directory, filename)
    with open(path, "w") as f:
        return json.dump(data, f)

def getting_all_email_ids(api_key: str) -> List:
    #calling hubspot api to get the information that we want
    emails_list: list = []
    limit = 100
    get_all_emails_url = "https://api.hubapi.com/marketing-emails/v1/emails?"
    #publish date greater than 30th June 2018 to not retrieve data from draft emails
    parameter_dict = {'hapikey': api_key, 'limit':limit, 'publish_date__gte': 1530309600000}
    parameter_dict['offset'] = 0
    headers: Dict = {}
    # Paginate your request using limit
    while True:
        parameters = urllib.parse.urlencode(parameter_dict)
        get_url = get_all_emails_url + parameters
        r = utilities.get_with_retries(get_url, headers, 2, 3)
        response_dict = r.json()
        emails_list.extend(response_dict['objects'])

        if response_dict["offset"] >= response_dict['total']:
            break
        else:
            parameter_dict['offset'] = response_dict['limit']+response_dict['offset']

    ids: List = []
    for item in emails_list:
        if 'campaignName' in item:
            if item['isPublished'] == True and item['ab'] == False:
                ids.append(str(item['id']))
    print("list from ids has {} results".format(len(ids)))
    return ids

def dump(directory: str, api_key_path: str) -> None:
    #dumping all the email ids to a file
    api_key = utilities.load_api_key_from_file(api_key_path)
    email_ids = getting_all_email_ids(api_key)
    email_ids_to_file(directory, email_ids)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="create a file with all email ids."
    )

    parser.add_argument(
        "--directory",
        required=True,
        type=str,
        help="path to directory to write the files")

    parser.add_argument(
        "--api_key_path",
        required=True,
        type=str,
        help="path to credentials")

    args = parser.parse_args()

    dump(args.directory, args.api_key_path)
