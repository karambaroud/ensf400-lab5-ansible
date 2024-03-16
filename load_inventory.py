#! /usr/bin/env python3
# File Name: load_inventory.py
# Assignment: 2
# Completed by: Karam Baroud
# Submission Date: March 16, 2024


import ansible_runner
import re

# Call the get_inventory function to get inventory name and group
inv_response, error = ansible_runner.interface.get_inventory(
    action='list',
    inventories=['./hosts.yml'],
    response_format='json',
    quiet=True
)

ip_response, error, code = ansible_runner.interface.run_command("ansible-playbook", [
        "-i", "./hosts.yml",
        "--private-key", "./secrets/id_rsa", 
        "./find_ip_playbook.yml"
    ],
    quiet=True
)

if code != 0:
    print("Error running the playbook")
    print(error)
    exit(1)

# isolate the IP addresses from the response using regex
    # seem to always be in correct order
ip_regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
ip_addresses = re.findall(ip_regex, ip_response)

# Print host content
i = 0
for host in inv_response["_meta"]["hostvars"]:
    print(f"Host: {host}")
    print(f"IP: {ip_addresses[i]}")
    print(f"Group: {'loadbalancer' if host == 'localhost' else 'app_group'}")
    print()
    i += 1

ansible_runner.interface.run_command("ansible", [
    "-i", "./hosts.yml",
    "--private-key", "./secrets/id_rsa",
    "all:localhost",
    "-m", "ping"
])