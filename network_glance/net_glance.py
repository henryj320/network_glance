"""Module to return the devices connected to the network."""
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


if __name__ == '__main__':
    run()
