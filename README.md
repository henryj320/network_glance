# network_glance

Last update: 2023-03-31 23:27
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

To run the project, follow these steps:
1. Clone the Git repository with ` git clone git@github.com:henryj320/network_glance.git `.
2. Move to the repository file with ` cd network_glance `.
3. Create a new virtual environment with ` python -m venv venv ` and ` . ./venv/bin/activate `.
4. Install build with ` pip install --upgrade build `.
5. Build the package with ` python -m build `.
6. Download all requirements with ` pip install . `.
7. Run the API with sudo permissions - ` sudo python basic_viewer/api.py `.
    - This requires ` sudo ` permissions as it sends packets on the network.
8. View the website by opening "basic_viewer/*index.html*".

### Running Tests
To test the code after making changes, run the following commands:
``` bash
cd network_glance
tox  # Runs pycodestyle and pydocstyle.

sudo rm -rf .tox
sudo tox -e tests  # Builds the project. Also runs tox and pytests
```
