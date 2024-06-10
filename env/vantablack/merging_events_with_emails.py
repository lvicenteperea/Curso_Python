import json
import argparse
import os
import pandas as pd
from typing import Any

def getting_data_to_join(directory_path: str) -> Any:
    #loading files to use in our function
    directory_files = os.listdir(directory_path)
    for file in directory_files:
        if file.endswith(".json"):
            json_path = os.path.join(directory_path, file)
            with open(json_path) as read_from_directory:
                data =  json.load(read_from_directory)
                yield (data)

def data_to_csv(directory_emails: str, directory_events: str, filename:str):
    emails = []
    events = []
    for email_data in getting_data_to_join(directory_emails):
        for email in email_data:
            emails.append(email)
    for events_data in getting_data_to_join(directory_events):
        for event in events_data:
            events.append(event)
    #creating the datasets to join
    emails_data = pd.DataFrame(emails)
    events_data = pd.DataFrame(events)
    #merging on primaryEmailCampaignId
    joining_data = emails_data.merge(events_data, on='primaryEmailCampaignId', how='inner')
    #csv to directory
    joining_data.to_csv(filename, sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Load event and email data and create an output join file."
    )

    parser.add_argument(
        "--directory_emails",
        required=True,
        type=str,
        help="path to directory to load email data")

    parser.add_argument(
        "--directory_events",
        required=True,
        type=str,
        help="path to directory to load events data")

    parser.add_argument(
        "--filename",
        required=True,
        type=str,
        help="name for csv file")

    args = parser.parse_args()

    data_to_csv(args.directory_emails, args.directory_events, args.filename)
