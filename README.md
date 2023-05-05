# network_glance

Last update: 2023-05-05 13:27
<br><br>

## network_glance

**Title**: network_glance

**Date Started**: 2023-03-17

**Date Completed**: 2023-03-31

**Language**: Python

**Overview**: Script to output various details about the network and hardware connected to the network. Including:
- Devices connected to Network: Name, IP, Time connected for
- Personal Devices: Name, Status, Last Online
- Endpoints: Name, Status
The intention would be for the output of this to be used in React Dashboard with a traffic-light system.

---

### Running the Project

#### With Docker
Running Network Glance is very easy if you use docker. Simply follow these steps:
1. Clone the Git repository with ` git clone git@github.com:henryj320/network_glance.git `.
2. Update "network_glance/assets/*device_map.json*" and "network_glance/assets/*last_online.json*" with your own devices.
3. Update the IP address within these files to match your system's IP address:
    - *docker-compose.yml*
    - "basic_viewer/*index.html*"
    - "basic_viewer/*api.py*"
4. Move to the repository file with ` cd network_glance `.
5. Update the endpoints to check inside of "basic_viewer/*api.py*".
6. Run the two containers (website and API) with **` docker compose up -d `**.
7. Visit ` http://<ip-address>:1001/ `.

#### Without Docker
To run the project, follow these steps:
1. Clone the Git repository with ` git clone git@github.com:henryj320/network_glance.git `.
2. Update "network_glance/assets/*device_map.json*" and "network_glance/assets/*last_online.json*" with your own devices.
3. Update the IP address within these files to match your system's IP address:
    - *docker-compose.yml*
    - "basic_viewer/*index.html*"
    - "basic_viewer/*api.py*"
4. Move to the repository file with ` cd network_glance `.
5. Create a new virtual environment with ` python -m venv venv ` and ` . ./venv/bin/activate `.
6. Install build with ` pip install --upgrade build `.
7. Build the package with ` python -m build `.
8. Download all requirements with ` pip install . `.
9. Run the API with sudo permissions - ` sudo python basic_viewer/api.py `.
    - This requires ` sudo ` permissions as it sends packets on the network.
10. View the website by opening "basic_viewer/*index.html*".

### Running Tests
To test the code after making changes, run the following commands:
``` bash
cd network_glance
tox  # Runs pycodestyle and pydocstyle.

sudo rm -rf .tox
sudo tox -e tests  # Builds the project. Also runs tox and pytests
```
