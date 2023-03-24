# from network_glance import net_glance as net_g  # ` pip install . ` required to work.
import net_glance as net_g
import click

@click.command()
@click.argument("devices", required=True, nargs=-1)  # Takes 0+ arguments of hostnames.

def run(devices: list):

    devices_online = net_g.run()  # Returns a dict of all devices connected to the network.
    devices_online = devices_online["devices"]


    input_devices = []
    for device in devices:  # Converts the devices tuple to a list.
        input_devices.append(device)

    personal_devices = []

    for input_device in input_devices:  # Checks whether each input is currently online

        for online_device in devices_online:

            if input_device == online_device["name"]:

                personal_devices.append({
                    "name": online_device["name"],
                    "ip": online_device["ip"],
                    "connected": True
                    # "mac": online_device["mac"]
                })

                input_devices.remove(input_device)

    
    for offline_device in input_devices:  # input_devices now only contains offline devices.
        personal_devices.append({
            "name": offline_device,
            "connected": False
        })



    response = {
        "personal_devices": personal_devices
    }

    print(response)

    return response


if __name__ == '__main__':

    response = run()
