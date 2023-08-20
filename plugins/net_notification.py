#!/usr/bin/env python3

import subprocess

def get_network_interfaces():
    interfaces_output = subprocess.check_output("ip link show | grep 'state UP'", shell=True).decode()
    interfaces = interfaces_output.strip().split("\n")
    return interfaces

def get_network_status(interface_count):
    if interface_count < 3:
        return "OK"
    elif 3 <= interface_count <= 4:
        return "WARN"
    else:
        return "CRITICAL"

if __name__ == "__main__":
    network_interfaces = get_network_interfaces()
    interface_count = len(network_interfaces)

    status = get_network_status(interface_count)

    output = []
    output.append("<<<network_status>>>")
    output.append(f"status: {status}")

    print("\n".join(output))
