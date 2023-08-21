#!/usr/bin/env python3

import json
import os
import sys
import time

def create_notification_file(alert_id, hostname, service_output, long_service_output):
    timestamp = int(time.time())
    filename = f"~/tmp/{timestamp}_{alert_id}.log".replace("~", os.path.expanduser("~"))

    notification_data = {
        "monitoringInfo": {
            "monitoringObjectHostname": hostname,
            "monitoringObjectSource": "CheckMK",
            "monitoringObjectAlertDescription": service_output,
            "monitoringObjectAlertFullDescription": long_service_output,
        }
    }

    with open(filename, "w") as file:
        json.dump(notification_data, file, indent=4)

def main():
    if len(sys.argv) < 5:
        print("Usage: custom_notification_plugin.py <alert_id> <hostname> <service_output> <long_service_output>")
        sys.exit(1)

    alert_id = sys.argv[1]
    hostname = sys.argv[2]
    service_output = sys.argv[3]
    long_service_output = sys.argv[4]

    create_notification_file(alert_id, hostname, service_output, long_service_output)

if __name__ == "__main__":
    main()
