import unittest
import os
import tempfile
import json
from typing import Any
from vantablack import email_ids_to_file
from vantablack import email_statistics_to_directory
from vantablack import email_click_events_to_directory

def read_from_file(file_path: str) -> Any:
    with open(file_path) as read_from_file:
        return json.load(read_from_file)

class Test(unittest.TestCase):
    def test_email_ids_to_file(self):
        # this creates a temporary directory for testing: this way we don't
        # leave crap all over the file system
        with tempfile.TemporaryDirectory() as temp_dir:
            data = ['10000', '20000']
            path = os.path.join(temp_dir, 'emails_ids.json')
            email_ids_to_file.email_ids_to_file(temp_dir, data)
            testing_loading_data = read_from_file(path)
            self.assertEqual(data, testing_loading_data)

    def test_marketing_emails_to_directory(self):
        # this creates a temporary directory for testing: this way we don't
        # leave crap all over the file system
        with tempfile.TemporaryDirectory() as temp_dir:
            data = [{'primaryEmailCampaignId':123, 'email_id': 123}]
            email_statistics_to_directory.marketing_emails_to_directory(temp_dir, data, 'test.json')
            testing_loading_data = email_click_events_to_directory.iterate_over_campaign_id(temp_dir)
            for test in testing_loading_data:
                self.assertEqual(123, test)
