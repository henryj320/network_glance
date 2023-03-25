"""Module to return the devices connected to the network."""
import datetime
import json
import scapy.all as scapy

json_file = "./network_glance/assets/device_map.json"


def run() -> dict:
    """Gather details on each device connected to the network..

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
            update_last_online("./network_glance/assets/last_online.json", hostname_lookup[1])

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


def update_last_online(json_file, alias: str) -> bool:

    # Loads the last online .json file.
    last_online_file = open(json_file, "r")
    last_online_mappings = json.load(last_online_file)



    current_time = datetime.datetime.now()

    last_online_file = open(json_file, "w")

    # Sets online devices last_online as now.
    last_online_mappings[alias][0] = str(current_time)

    json.dump(last_online_mappings, last_online_file, indent=2)


    print("Last online for " + alias + " was updated.")

    return


if __name__ == '__main__':
    run()
