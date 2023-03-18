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
