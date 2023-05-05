# network_glance

Last update: 2023-05-05 13:23
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
    - Ending with
        - ` fuser -k 4000/tcp `
    - Trying to add a black border to the loading bar.
        - Looks good!
13. Adding last online
    - Made it so device_map updates last_online.json for any devices that are online.
    - Making net_glance do the same.
    - Hard to update basic_viewer
        - Because it doesn't call the device_glance script at the moment.
14. Adding last online to basic_viewer
    - Going to try it with a fetch command
        - To fetch the content of last_online.json
        - Having some issues with it not retrieving first
            - Doing it first. May need an await
                - That isnt the issue
                - For some reason it is undefined when it shouldnt be
        - The arrays are slightly different somehow
            - ['henry-ubuntu-surface-3', 'henry-android-phone'] != ['henry-ubuntu-surface-3', 'henry-android-phone']
                - I dont understand why
            - Length of offline_devices_last_online and offline_devices do not match even though they should
    - Tried changing the layout of last_online.json (shown in last_online_alt.json)
    - Array.isArray(offline_devices_last_online) returns true
    - offline_devices_last_online.push(response.lastOnline[y].name)
        - That isnt working properly
            - Doesnt work pushing "1" either
    - Works when inside the fetch statement. So weird...
    - Code cleanup required
    - Running the website doesnt update last_online. Probably linked to the JSON file path being wrong when hosting from the server. Add a parameter
        - Fixed that
    - Update net_glance and device_glance to use the new format
        - Updated net_glance#
        - Updated device_glance
        - Checking it updates when website runs
            - TypeError: run() takes 0 positional arguments but 1 was given
                - ` pip install . `
                - Didnt work
                - ` python -m build `
                - `python install . `
                - `python install .[testing] `
                - `python install .[viewer] `
                - Still giving the error
                    - Not quite sure as to why
                - Deleting __pycache__
                - ` sudo pip install . `
                    - That did it! Needed to pip install the latest version
            - Now it seems to run infinitely
                - ` sudo python ./network_glance/net_glance.py `
                    - That doesnt cause it
                - ` curl http://192.168.1.101:4000/monitor/net_glance `
                    - That is doing it repeatedly!
                        - Not the if __main__ part
        - TODO: Diagnose why net_glance now repeatly runs
            - Went to bed for the night.
            - Retried the ` curl `. Didnt repeat
            - Running the website. That does repeat!
            - Curl does not. So its an issue with the website somehow
                - Something to do with the fetch?
            - Commented out the fetch. It still does it...
            - Seems to refresh just after printing out the fetch
            - Doesnt repeat if I dont click go live (and just drag the file to browser)
                - So its just an issue with going live. Great! That's fine then
                - Restarted the laptop. Still an issue with "Go Live"
        - Access to fetch at 'file:///home/henry/Documents/Git_Repos/network_glance/network_glance/assets/last_online_alt.json' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, isolated-app, chrome-extension, chrome, https, chrome-untrusted
            - Added https://mybrowseraddon.com/access-control-allow-origin.html?v=0.1.8&type=install Extension
            - Tried setting mode to CORS in the fetch
            - Could just have a "get file" method in the API
        - Is it to do with live reload?
    - Trying to fix the Live reload issue
        - Checking if its the same on main branch
            - Issue is not there. What are the differences?
                - Comparing the differences
                - Theres nothing that should cause a loop
        - OH! IS IT BECAUSE LAST_ONLINE.JSON is updating?
            - Adding last_online.json to the Ignore
            - Yes! That's it. To fix it, just go into the settings of Live Server and add the file to the liveServer.settings.ignoreFiles array.
15. Title attribute
    - Interesting addition. Each HTML element can have a title="" attribute
        - Text to show on hover
    - Added title to many fields.
16. Toxing
    - Code cleanup
        - device_glance.py
17. Adding to the website
    - ` sudo fuser -k 4000/tcp `
    - Added a drop-shadow
    - Adding a progress bar
    - Adding an error if no connection.
18. Writing tests
    - Figuring out what could be in the tests.
    - Might have an issue running tests as sudo
        - ` sudo apt install python3.10-venv `
        - Fine after that. May mess up tox testing
    - Running tox
        - Failed
        - Deleted the ".tox" folder.
    - Found one issue:
        - On failed update_last_online() it deletes last_online.json content.
    - Runs with ` sudo tox -e tests `.
    - Moving onto *test_device_glance.py*
        - Running get_last_online() on its own seemed to append to last_online.json, not overwrite
    - test_device_glance.py complete. Toxed too
    - Likely an issue that it needs to be run as sudo.
    - Moving onto *test_endpoint_glance.py*
        - Think its all working
19. Running tests in the pipeline
    - FAILED network_glance/tests/test_net_glance.py::test_ng_run - PermissionError: [Errno 1] Operation not permitted
    - FAILED network_glance/tests/test_endpoint_glance.py::test_eg_run - requests.exceptions.ConnectTimeout: HTTPConnectionPool(host='192.168.1.109', port=4000): Max retries exceeded with url: /not_real (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x7f2546099540>, 'Connection to 192.168.1.109 timed out. (connect timeout=None)'))
    - May need to just run it locally
    - Failed
        - ` sudo rm -rf .tox `
20. Final finishing touches.
    - Code cleanup
        - Python files first
        - index.html
    - Added a navbar
    - Smooth scrolling
    - "Wait" cursor whilst loading
    - Added to the README.
21. Testing all the steps work
    - One issue "TypeError: Failed to fetch" on the Devices Table.
    - Failed to fetch the fike :/

### Dockerising Development Notes

22. Checking that it still works just in case.
    - ` . ./venv/bin/activate `
    - ` sudo fuser -k 4000/tcp `
    - ` sudo python basic_viewer/api.py `
    - Clicking "Go Live" on the index.html
    - Cant connect to the API for some reason
        - Ah, the React Dashboard was using the same ports
    - Yep, all works fine
23. Converting the website to Docker
    - Creating the *website.Dockerfile*
        - Based on http://tecadmin.net/tutorial/docker-run-static-website
    - ` sudo docker build -f website.Dockerfile -t network-glance-website-image . `
    - ` sudo docker run -it -d -p 8081:80 network-glance-website-image `
    - Working. Fails because of the API but thats good!
24. Converting the API to Docker
    - Creating an *api.Dockerfile* file
        - Added pip installing
    - Made a requirements.txt file
        - Found the requirements in the project
        - Set versioning too
    - Trying to run it
        - ` cd .. `
        - ` sudo docker build -f api.Dockerfile -t network-glance-api-image . `
        - ` sudo docker run network-glance-api-image `
    - Adding the rest of the lines
    - Trying to run it
        - ` sudo docker build -t network-glance-api-image --no-cache -f api.Dockerfile . `
        - ` sudo docker run --publish 4000:4000  network-glance-api-image `
    - Nope, need to pip install it.
        - Needed to change the *pyproject.toml* version from 3.9 to 3.8
    - Seems to be working!
25. Writing a Docker Compose
    - It all works! I do need to choose Port numbers, though
    - Changing ports to 1002 (API) and 1001 (website)
    - Removing all containers and images
26. Getting scapy working
    - Everything is running, but scapy is running inside a container so cannot see the network
    - I wonder whether --network=host would work?
        - ` sudo docker run --publish 1002:1002 --network=host network_glance-api `
            - That works
    - Adding to *docker-compose.yml*
        - ` network_mode: host `
27. Updating the *README.md* with Docker information
28. Updated the *README.md* with the IP Address locations that need to be updated.
    - At some point, this will become an .env file.
