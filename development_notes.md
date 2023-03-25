# network_glance

Last update: 2023/03/24 00:42
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
7. Adding Tox
    - ` tox quickstart .`
    - Adding testing
        - To install net_glance and then run tests on it as if it were a pip module.
    - Use these commands to view:
        - ` tox `
        - ` tox -e tests `
        - ` tox -e dependencies `
    - Fixed pycodestyle and pydocstyle issues.
8. Added a CI/CD pipeline which runs the same checks as ` tox -e tests `.
9. Starting Device glance
    - Trying to take a list as an input.
    - Example command to run it:
        - ` python network_glance/device_glance.py home-router henry-alexa henry-windows-gaming-pc poppy-alexa henry-armbian-rpi-4-model-b henry-firestick `
    - sudo running it makes it so that network_glance isnt recognised
    - ` deactivate `
    - ` pip install . `
    - Still not finding network_glance
    - I'll do it the dull way for now
    - Working device_glance.
10. Moving on to endpoint_glance
    - ` curl 192.168.1.109:4000/muscle_checker `
    - https://www.nylas.com/blog/use-python-requests-module-rest-apis/
    - Can run it with:
    ` python network_glance/endpoint_glance.py http://192.168.1.109:4000/not_real http://192.168.1.109:4000/muscle_checker `.
    - Running ` tox `.
    - ` python -m build `
    - ` pip install -e . `
    - ` pip show network_glance `
    - Failed because device_glance didnt import correctly.
        - Keep getting module not found errors.
    - Maybe set up a class to import instead
        - https://realpython.com/absolute-vs-relative-python-imports/
    - Or maybe just take the output of net_glance as an input.
        - Have a parent "main.py" module that imports the others
            - Gives the output of one as an input to others
        - Then testing just does imports the same way
        - Fixing device_glance.py
            - Now runs with ` sudo python network_glance/device_glance.py {} henry-android-phone `.
11. Fixing everything into a main.py module
    - No more importing each within other modules
        - Instead, main.py imports all of them.
    - Tested and linted. Should work.
12. Making the basic viewer
    - Axios calls are the same in vanilla JS.
    - Added "viewer" requirements to pyproject.toml
    - ` python ./basic_viewer.api.py `
        - When accessing, returns Operation not permitted
    - ` sudo python ./basic_viewer.api.py `
        - No Module named 'flask'
            - Is it cused by root not having the python path
    - Looks like sudo uses a different instance of python
        - ` python3 -c "import sys; print(sys.path)" `
    - Tried elevating to root
        - ` su root `.
            - Can't get my password...
            - ` sudo usermod -U root `
            - ` chmod u+s /bin/su `
    - ` which python `
        - /home/henry/anaconda3/lib/python3.9
        - Python 3.9.13
    - ` sudo which python `
        - /usr/bin/python
        - Python 3.10.6
    - ` sudo alias python='/home/henry/anaconda3/lib/python3.9' `
        - Can use ` unalias ` to remove it
        - alias: Command not found
            - ` sudo apt-get install bash `
    - ` . ~/.bashrc `
    - ` alias python='/usr/bin/python' `
        - Setting it to the old one
        - ` pip install . `
        - ` unalias python `
        - Didn't fix the issue
        - ` python -m pip install .[viewer] `
        - ` python -m pip list `
        - No module named Flask.
        - ` sudo pip list `
            - Doesn't have it
        - ` sudo pip install flask `
            - That worked
        - Can now connect to the server
            - ` sudo python ./basic_viewer/api.py `
        - For some reason, Dev_glance is not returning the correct responses.
            - Changing from Tuple to array
            - Tried adding it as a global variable
    - Just do it using the network table instead
        - Checks if online device == personal device
        - If not, set to offline
    - Added the endpoints table
        - Same issue. Its saying one is offline for some reason
        - Its because of the "if true bit"
    - Added a really cool loading screen!
    - toxing
