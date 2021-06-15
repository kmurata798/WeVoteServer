from django.urls import reverse
from django.test import TestCase
from datetime import datetime

import json

class WeVoteAPIsV1TestsPositionListForBallotItem(TestCase):
    databases = ["default", "readonly"]

    def setUp(self):
        self.position_list_for_ballot_item_url = reverse("apis_v1:positionListForBallotItemView")

    def test_retrieve_with_no_ballot_item_id(self):
        response = self.client.get(self.position_list_for_ballot_item_url)
        json_data = json.loads(response.content.decode())

        self.assertEqual('status' in json_data, True, "status expected in the json response, and not found")

        self.assertEqual(json_data['status'].strip(),
                         "POSITION_LIST_RETRIEVE_MISSING_BALLOT_ITEM_ID",
                         f"Received status: {json_data['status']}\nExpected status: POSITION_LIST_RETRIEVE_MISSING_BALLOT_ITEM_ID")

        self.assertEqual(json_data['success'],
                         False,
                         f"Received success: {json_data['success']}\nExpected success")

        self.assertEqual(json_data["count"], 0,
                         f"Received count: {json_data['count']}\nExpected count: 0")
