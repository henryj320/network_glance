"""Main module of network_glance."""
import net_glance as net_g
import device_glance as dev_g
import endpoint_glance as end_g


def run():
    """Run device_glance, net_glance and endpoint_glance."""
    network = run_net_glance()

    print("")
    print("Devices Connected to Network:")
    print(network["devices"])

    print("")
    print("Status of Personal Devices:")
    personal_devices = ["henry-armbian-rpi-4-model-b", "henry-android-phone", "henry-windows-gaming-pc"]
    print(run_dev_glance(network, personal_devices))

    print("")
    print("Status of Endpoints:")
    endpoints = ("http://192.168.1.109:4000/not_real",
                 "http://192.168.1.109:4000/muscle_checker")
    print(run_end_glance(endpoints))
    print("")


def run_net_glance() -> dict:
    """Run the net_glance module and returns the output.

    Returns:
        dict: The devices connected to the network.
    """
    return net_g.run()


def run_dev_glance(network: dict, personal_devices: tuple) -> dict:
    """Run the device_glance module and returns the output.

    Args:
        network (dict): The devices connected to the network.
        personal_devices (tuple): The devices that you need the status of.

    Returns:
        dict: The status of the given personal_devices.
    """
    return dev_g.run(network, personal_devices)


def run_end_glance(endpoints: tuple) -> dict:
    """Run the endpoint_glance module and return the output.

    Args:
        endpoints (tuple): The endpoints that you need the status of.

    Returns:
        dict: The status of the given endpoints.
    """
    return end_g.run(endpoints)


if __name__ == '__main__':
    response = run()
