# network_glance

Last update: 2023-05-11 16:16
<br><br>

## Releases for network_glance
This document provides details on the Network Glance releases.

---

### Release V1.0.0 (March 2023)
This is the initial release for Network Glance. The project's current functionality is:

#### Dockerised
This project is dockerised within two containers (website and API) for easy starting/stopping of services.

#### Net Glance
The Net Glance script returns all of the devices on the network and makes use of the *device_map.json* file to map the MAC address to a hostname. Net Glance also updates the *last_online.json* file to state that the device is currently online.

#### Device Glance
This script allows the user know whether a collection of specific devices are currently on the network or not. If the device is not online, it will return the last online time based on *last_online.json*.

#### Endpoint Glance
The Endpoint Glance script sends GET requests to any given endpoints and returns whether the endpoint returned a 200 or not.

#### Basic Viewer
This has two parts - the website and the API. Together, they show a website which outputs the results of Net Glance, Device Glance and Endpoints in tables.

---
