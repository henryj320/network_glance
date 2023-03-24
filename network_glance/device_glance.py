"""Module to return whether given hostnames are currently connected."""


def run(network: dict, devices: tuple) -> dict:
    """Check whether given devices are connected to the network or not.

    Args:
        devices (tuple): 0 or more devices to check.

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
                    "connected": True
                    # "mac": online_device["mac"]
                })

                input_devices.remove(input_device)

    for offline_device in input_devices:  # Adds each offline device.
        personal_devices.append({
            "name": offline_device,
            "connected": False
        })

    response = {
        "personal_devices": personal_devices
    }

    return response


if __name__ == '__main__':
    response = run()
