import ansible_runner
import json

inventoryJSON = ansible_runner.get_inventory("list", ["./hosts.yml"], quiet=True)

inventory = json.loads(inventoryJSON[0])

for host in inventory["app_group"]["hosts"]:
    # print(hosts)
    print("\nHost name: " + host)
    print("IP address: " + inventory["_meta"]["hostvars"][host]["ansible_host"])
    print("Group: app_group")

ansible_runner.interface.run_command("ansible", ["-i", "./hosts.yml", "all", "-m", "ping"])

