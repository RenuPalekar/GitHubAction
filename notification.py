import json
from datetime import datetime, timedelta, timezone
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
# install - pip install slack_sdk
import requests


# Read data from JSON file
with open('spp.json') as json_file:
    data = json.load(json_file).get('Members', [])


def send_slack_notification(token, channel, message):
    client = WebClient(token=token)

    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
        print(f"Slack notification sent successfully: {message}")
    except SlackApiError as e:
        print(f"Error sending Slack notification: {e.response['error']}")


def notify(bundle_id, spp_id, release_date, token, channel):
    notification_format = f"Bundle ID: {bundle_id} SPP ID: {spp_id} Release Date: {release_date}"

    # Implement Slack notification and email sending here
    send_slack_notification(token, channel, notification_format)


def check_and_notify(data):
    present_date = datetime.now(timezone.utc)
    print(present_date)

    for bundle in data:
        bundle_id = bundle["BundleId"]

        spp_id = bundle.get("SPPId", "Not provided")
        release_date_str = bundle["ReleaseDate"]

        try:
            release_date = datetime.fromisoformat(release_date_str)
            release_date = release_date.replace(tzinfo=timezone.utc)  # Make release date offset-aware
        except ValueError:
            # Handle invalid date format
            print(f"Invalid date format for Bundle ID {bundle_id}")
            continue

        age_in_month = (present_date - release_date).days // 30
        print(f"age in months {age_in_month}")

        if age_in_month > 18:  # Checking if older than 18 months
            notify(bundle_id, spp_id, release_date_str, "YOUR_SLACK_TOKEN", "#your_channel_name")
        else:
            print(f"bundle id {bundle_id} is not older than 18 months")


check_and_notify(data)
