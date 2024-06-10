import argparse
import json
import urllib.parse
import os
from typing import Any, Iterable, Dict, List
from vantablack import utilities

def iterate_over_campaign_id(directory_path: str) -> Iterable[Dict]:
    #iterate through files in directory to extract primaryEmailCampaignId
    directory_files = os.listdir(directory_path)
    for file in directory_files:
        if file.endswith(".json"):
            json_path = os.path.join(directory_path, file)
            with open(json_path) as read_from_directory:
                for data in json.load(read_from_directory):
                    yield (data['primaryEmailCampaignId'])

def make_email_events(url: str, date: Any, primaryEmailCampaignId: str, eventId: str, email_user: str) -> Dict:
    return {
    #dictionary with information needed
    'url': url,
    'date': date,
    'primaryEmailCampaignId': primaryEmailCampaignId,
    'eventId': eventId,
    'email_user':email_user
    }

def email_events_to_directory(directory: str, data: Any, filename: Any) -> None:
    #creating files in a directory with the email event data
    path = os.path.join(directory, filename)
    with open(path, "w") as f:
        return json.dump(data, f)

def get_campaign_events(api_key: str, campaign_id: Dict, event_type: str) -> List:
    #calling hubspot api to get email events data
    get_all_events_url = "https://api.hubapi.com/email/public/v1/events?"
    limit = 1000
    parameter_dict = {'hapikey': api_key, 'campaignId': campaign_id, 'eventType': event_type, 'limit':limit}
    headers: Dict = {}
    campaigns_events: List = []
    while True:
        parameters = urllib.parse.urlencode(parameter_dict)
        get_url = get_all_events_url + parameters
        r = utilities.get_with_retries(get_url, headers, 2, 3)
        response_dict = r.json()
        if response_dict is not None:
            campaigns_events.extend(response_dict["events"])
            parameter_dict['offset'] = response_dict['offset']
            if response_dict["hasMore"] == False:
                return campaigns_events

def getting_email_events_data(api_key: str, campaign_id: Dict, event_type: str) -> List:
    campaign_events = get_campaign_events(api_key, campaign_id, event_type)
    events_data = []
    for item in campaign_events:
        #creating the dictionary
        events = make_email_events(
            url = item['url'],
            date = item['created'],
            primaryEmailCampaignId = item['emailCampaignId'],
            eventId = item['id'],
            email_user=item['recipient'])
        events_data.append(events)
    print("list from events has {} results".format(len(events_data)))
    return events_data

def dump(directory: str, directory_ids_path: str, api_key_path: str, eventType: str) -> None:
    #dumping all click events to files in directory
    api_key = utilities.load_api_key_from_file(api_key_path)
    campaign_ids = iterate_over_campaign_id(directory_ids_path)
    for campaign_id in campaign_ids:
        if campaign_id != 0:
            email_events = getting_email_events_data(api_key, campaign_id, eventType)
            if len(email_events) != 0:
                email_events_to_directory(directory, email_events, "{}.json".format(campaign_id))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Create a list with all click events by campaign and dump them to an output file in a directory."
    )

    parser.add_argument(
        "--directory",
        required=True,
        type=str,
        help="path to directory to write the files")

    parser.add_argument(
        "--directory_ids_path",
        required=True,
        type=str,
        help="path to directory where to extract primaryEmailCampaignId")

    parser.add_argument(
        "--api_key_path",
        required=True,
        type=str,
        help="path to credentials")

    parser.add_argument(
        "--eventType",
        required=True,
        type=str,
        help="type of event that we want to extract")

    args = parser.parse_args()

    dump(args.directory, args.directory_ids_path, args.api_key_path, args.eventType)
