# from network_glance import net_glance as net_g  # ` pip install . ` required to work.
import net_glance as net_g
import click

@click.command()
@click.argument("devices", required=True, nargs=-1)  # Takes 0+ arguments of hostnames.

def run(devices: list):

    online_devices = net_g.run()

    print(online_devices)
    print("")
    print(devices)


if __name__ == '__main__':
    run()