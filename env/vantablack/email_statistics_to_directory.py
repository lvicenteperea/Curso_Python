import argparse
import json
import urllib.parse
import os
from typing import Any, Dict, List, Optional
from vantablack import utilities

def load_email_id(file_path: str) -> str:
    #load email ids from list
    with open(file_path) as read_from_file:
        data = json.load(read_from_file)
        return data

def marketing_emails_to_directory(directory: str, data: Any, filename: Any) -> None:
    #writing email data to files in directory
    path = os.path.join(directory, filename)
    with open(path, "w") as f:
        return json.dump(data, f)

def make_statistics_dict(
    #function to create the dictionary with only the information that we need
    email_name: str, email_id: str, campaign_name: str, campaign_id: str, primaryEmailCampaignId:str, subject: str, publishDate: Any,
    sent: Any, open: Any, delivered: Any, bounce: Any, unsubscribed: Any, click: Any, notsent: Any, hardbounced: Any,softbounced: Any) -> Dict:
    return {
    'email_name': email_name,
    'email_id': email_id,
    'campaign_name': campaign_name,
    'campaign_id': campaign_id,
    'primaryEmailCampaignId': primaryEmailCampaignId,
    'subject': subject,
    'publishDate': publishDate,
    'sent': sent,
    'open': open,
    'delivered': delivered,
    'bounce': bounce,
    'unsubscribed': unsubscribed,
    'click': click,
    'notsent': notsent,
    'hardbounced': hardbounced,
    'softbounced': softbounced
    }

def getting_email_statistics(api_key: str, email_id: str) -> Optional[List]:
    #calling hubspot api to get the information that we want
    get_marketing_emails_with_statistics = "https://api.hubapi.com/marketing-emails/v1/emails/with-statistics/"
    parameter_dict = {'hapikey': api_key}
    headers: Dict = {}
    parameters = urllib.parse.urlencode(parameter_dict)
    get_url = get_marketing_emails_with_statistics + email_id + "?" + parameters
    r = utilities.get_with_retries(get_url, headers, 2, 3)
    response_dict = r.json()
    email_data: List = []
    if 'campaignName' in response_dict and 'stats' in response_dict:
        if 'open' in response_dict['stats']['counters']:
            for campaign in response_dict['allEmailCampaignIds']:
                email_statistics = make_statistics_dict(
                email_name=response_dict['name'],
                email_id=response_dict['id'],
                campaign_name=response_dict['campaignName'],
                campaign_id=response_dict['campaign'],
                subject=response_dict['subject'],
                primaryEmailCampaignId=campaign,
                publishDate=response_dict['publishDate'],
                sent=response_dict['stats']['counters']['sent'],
                open=response_dict['stats']['counters']['open'],
                delivered= response_dict['stats']['counters']['delivered'],
                bounce=response_dict['stats']['counters']['bounce'],
                unsubscribed=response_dict['stats']['counters']['unsubscribed'],
                click=response_dict['stats']['counters']['click'],
                notsent=response_dict['stats']['counters']['notsent'],
                hardbounced=response_dict['stats']['counters']['hardbounced'],
                softbounced=response_dict['stats']['counters']['softbounced'])
            email_data.append(email_statistics)
    return email_data

def dump(directory: str, file_ids_path: str, api_key_path: str) -> None:
    #dumping all email data indivudally to file
    api_key = utilities.load_api_key_from_file(api_key_path)
    email_ids = load_email_id(file_ids_path)
    for email_id in email_ids:
        marketing_emails = getting_email_statistics(api_key, email_id)
        if marketing_emails != None:
            marketing_emails_to_directory(directory, marketing_emails, "{}.json".format(email_id))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="List files with email data in directory and dump them to an output file."
    )

    parser.add_argument(
        "--directory",
        required=True,
        type=str,
        help="path to directory to write the files")

    parser.add_argument(
        "--file_ids_path",
        required=True,
        type=str,
        help="path to directory where to extract email Ids")

    parser.add_argument(
        "--api_key_path",
        required=True,
        type=str,
        help="path to credentials")

    args = parser.parse_args()

    dump(args.directory, args.file_ids_path, args.api_key_path)
