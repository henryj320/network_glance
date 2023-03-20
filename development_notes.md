# network_glance

Last update: 2023/03/17 22:59
<br><br>

## Development notes for network_glance

1. Set up the repo.
    - Using pyproject.toml instead of setuptools
        - Documentation
            - https://godatadriven.com/blog/minimal-pyproject-toml-example/
            - https://github.com/pdm-project/tox-pdm/blob/main/pyproject.toml
            - https://python-poetry.org/docs/pyproject/
            - https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
            - https://github.com/pypa/sampleproject
            - https://packaging.python.org/en/latest/tutorials/packaging-projects/
        - Figuring out how it works
    - Testing whether it works
        - ` python -m venv venv `
        - ` . ./venv/bin/activate `
        - ` pip install . `
        - ` pip list `
        - ` pip uninstall network_glance `
        - ` pip install --upgrade build `
        - ` python -m build `
        - .
        - ` python -m build `
        - ` pip install . `
        - ` hello-world `
            - That works, but I dont think its how its meant to work
            - Looking at [this](https://packaging.python.org/en/latest/tutorials/packaging-projects/), that is how it should work
    - Figuring out optional dependencies
        - ` pip install .[testing] `
            - That then installs everything in the testing subfolder so you can run it anytime
    - Testing that I can then use it
        - ` pip install . `
        - ` python `
        - ` >>> from network_glance import network_glance_script as ng `
        - ` >>> ng.run `
2. Setting up the sprint board
3. Testing libraries
    - Testing who-is-on-my-wifi
        - ` wiom -d `
            - Shows info on this device
        - ` wiom -w `
            - Seems to require sudo permissions
    - Testing scapy
        - https://www.geeksforgeeks.org/network-scanning-using-scapy-module-python/?ref=rp
        - Used to make a packet
        - https://github.com/bwaldvogel/neighbourhood
4. Learning scapy
    - https://www.geeksforgeeks.org/how-to-build-a-wifi-scanner-in-python-using-scapy/?ref=rp
    - ` . venv/bin/activate `
    - ` pip install scapy `
    - ARP  
        - Address Resolution Protocol.
        - Connects a changing IP address to a (fixed) MAC address.
        - A directory holds a map of IP addresses and MAC addresses.
    - "No module named scapy"
        - When sudo running the python script
        - ` sudo apt-get install python3-scapy `
        - Now it works
        - Prints the devices on the network!
            - Basically broadcasts a packet and checks who responds
    - Trying to get the hostname too
        - Struggling. socket.gethostbyaddr() only works on localhost, not any of the others
        - Can nmap do it?
            - ` sudo nmap -sn 192.168.1.101/24 `
                - Nope. Returns IP and MAC address
5. Getting all the MAC addresses and (current) IPs
    - Checking whether they match the output of Scapy
        - Rpi matches
        - Gaming PC matches
        - Phone matches
        - Kindle Paperwhite does not match :/
        - Surface matches
    - Detected but missing from the Project board:
        - 192.168.1.113 - Fire TV
        - 192.168.1.102 - Henry Alexa
        - 192.168.1.115 - Poppy alexa
        - Added all
    - Added all to "assets/*device_map.json*".
6. Finishing net_glance.
    - Wrote lookup_hostname().
    - Made the run() method use it.
    - Having sets - {True, alias} was messing up. Switched to list.
    - Code cleanup.
    - Finished and merged in.
