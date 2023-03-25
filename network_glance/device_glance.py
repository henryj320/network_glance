"""Module to return whether given hostnames are currently connected."""
import datetime
import json



json_file = "./network_glance/assets/last_online.json"


def run(network: dict, devices: list) -> dict:
    """Check whether given devices are connected to the network or not.

    Args:
        devices (list): 0 or more devices to check.

    Returns:
        dict: Whether each device is online or not.
    """
    devices_online = network
    devices_online = devices_online["devices"]

    input_devices = []
    for device in devices:  # Converts the devices tuple to a list.
        input_devices.append(device)

    personal_devices = []

    for input_device in input_devices:  # Checks if inputs are online.

        for online_device in devices_online:

            if input_device == online_device["name"]:

                personal_devices.append({
                    "name": online_device["name"],
                    "ip": online_device["ip"],
                    "connected": True,
                    "last_online": str(datetime.datetime.now())
                    # "mac": online_device["mac"]
                })

                input_devices.remove(input_device)

    for offline_device in input_devices:  # Adds each offline device.
        personal_devices.append({
            "name": offline_device,
            "connected": False, 
            # Sets last_online to recorded in last_online.json
            "last_online": get_last_online(json_file, False, offline_device)
        })

    response = {
        "personal_devices": personal_devices
    }

    return response

def get_last_online(json_file: str, connected: bool, alias: str) -> str:

    # Loads the last online .json file.
    last_online_file = open(json_file, "r")
    last_online_mappings = json.load(last_online_file)



    if connected:
        last_online_file = open(json_file, "w")

        current_time = datetime.datetime.now()

        # Sets online devices last_online as now.
        last_online_mappings[alias][0] = str(current_time)

        # last_online = last_online_mappings[mac_address][0]

        json.dump(last_online_mappings, last_online_file, indent=2)

        print("Last online for " + alias + " was updated.")

        return str(current_time)
    
    try:
        last_online = last_online_mappings[alias][0]
    except KeyError:  # If MAC address not found in last_online.json.
        return "0000-00-00 00:00:01"
    
    return str(last_online)



    # print(last_online)

    # If connected = True
        # Returns now
        # Updates the file
    # Else, returns time in file

    return


if __name__ == '__main__':
    # response = run()

    get_last_online(json_file, True, "20:16:b9:90:2e:4b")
