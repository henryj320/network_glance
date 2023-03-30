"""Module to return the devices connected to the network."""
import datetime
import json
import scapy.all as scapy

json_file = "./network_glance/assets/device_map.json"
last_online_file = "./network_glance/assets/last_online.json"


def run(last_online_file: str) -> dict:
    """Gather details on each device connected to the network.

    Args:
        last_online_file (str): The relative path to the last_online.json file.

    Returns:
        dict: A dict containing the hostname, IP and MAC address
        of each device.
    """
    target_ip = "192.168.1.101/24"  # Destination IP Address (router).

    arp = scapy.ARP(pdst=target_ip)  # Creates an ARP packet.
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Ethernet broadcast packet.
    packet = ether/arp  # Stacks the two packets together.

    result = scapy.srp(packet, timeout=3)[0]  # "S"end and "R"eceive "P"ackets.

    clients = []
    for sent, received in result:  # For each response to the broadcast.
        hostname_lookup = lookup_hostname(json_file, received.hwsrc)

        clients.append({
            "name": hostname_lookup[1],
            "ip": received.psrc,
            "mac": received.hwsrc,
        })

        if hostname_lookup[1] != "Uknown Device":
            # Updates the last_online of all online devices.
            update_last_online(last_online_file,
                               hostname_lookup[1])

    return_dict = {
        "devices": clients
    }

    return return_dict


def lookup_hostname(json_file: str, mac_address: str) -> list:
    """Check the MAC-address from json_file to return the hostname and alias.

    Args:
        json_file (str): The relative path to the device_map.json file.
        mac_address (str): The MAC-address to lookup.

    Returns:
        list: A list containing whether the lookup succeeded, alongside
        the alias/hostname.
    """
    device_map_file = open(json_file)

    device_mappings = json.load(device_map_file)

    try:
        hostname = device_mappings[mac_address][0]
        alias = device_mappings[mac_address][1]
        return [True, alias]

    except KeyError as e:
        return [False, "Uknown Device"]


def update_last_online(json_file: str, alias: str) -> bool:
    """Update last_online.json with devices currently online.

    Args:
        json_file (str): The path of last_online.json.
        alias (str): The device's alias to update.

    Returns:
        bool: Success or Fail of update
    """
    last_online_file = open(json_file, "r")
    lo_map = json.load(last_online_file)
    # last_online_file.close()


    current_time = datetime.datetime.now()
    

    # Ensures that last_online.json is not emptied if the alias is invalid.
    valid_aliases = []
    for device in lo_map["lastOnline"]:
        valid_aliases.append(device["name"])
    
    if alias not in valid_aliases:
        return False


    last_online_file = open(json_file, "w")

    

    for index, value in enumerate(lo_map["lastOnline"]):

        if value["name"] == alias:
            lo_map["lastOnline"][index]["lastOnline"] = \
                str(current_time)

            json.dump(lo_map, last_online_file, indent=2)
            # print("Last online for " + alias + " was updated.")

            return True

    return False


if __name__ == '__main__':
    run(last_online_file)

    # update_last_online(last_online_file, "henry-armbian-rpi-4-model-b")
