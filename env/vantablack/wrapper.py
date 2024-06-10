import argparse
import tempfile
import os
from typing import Any
from vantablack import email_ids_to_file
from vantablack import email_statistics_to_directory
from vantablack import email_click_events_to_directory
from vantablack import merging_events_with_emails

EVENT = "CLICK"

def fetch_csv(api_key_path: str, filename:str) -> Any:
    with tempfile.TemporaryDirectory() as temp_dir:
        email_ids_dir = os.path.join(temp_dir, 'emails_directory')
        email_statistics_dir = os.path.join(temp_dir, 'email_statistics')
        email_statistics_filepath = os.path.join(email_ids_dir, 'emails_ids.json')
        email_events_dir = os.path.join(temp_dir, 'email_events')
        os.mkdir(email_ids_dir)
        os.mkdir(email_statistics_dir)
        os.mkdir(email_events_dir)
        email_ids_to_file.dump(email_ids_dir, api_key_path)
        email_statistics_to_directory.dump(email_statistics_dir, email_statistics_filepath, api_key_path)
        email_click_events_to_directory.dump(email_events_dir, email_statistics_dir, api_key_path, EVENT)
        merging_events_with_emails.data_to_csv(email_statistics_dir, email_events_dir, filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="wrapper for the package"
    )

    parser.add_argument(
        "--api_key_path",
        required=True,
        type=str,
        help="path to credentials")

    parser.add_argument(
        "--filename",
        required=True,
        type=str,
        help="name for csv file")
    args = parser.parse_args()

    fetch_csv(args.api_key_path, args.filename)
