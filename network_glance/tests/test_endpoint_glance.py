"""Testing script for net_glance. Run it with ` tox -e tests `."""
from network_glance import net_glance as net_g
from network_glance import device_glance as dev_g
from network_glance import endpoint_glance as end_g

import requests


def test_eg_run():

    valid_endpoints = ("http://192.168.1.109:4000/not_real",
                       "http://192.168.1.109:4000/muscle_checker")
    invalid_endpoints_port = ("http://192.168.1.109:4000/not_real",
                              "http://192.168.1.109:2028/fake")

    print(type(valid_endpoints))

    # Check it works if given valid inputs.
    result = end_g.run(valid_endpoints)
    assert len(result["endpoints"]) > 0

    # Check it fails if ports are closed
    try:
        result = end_g.run(invalid_endpoints_port)
        assert False
    except requests.exceptions.ConnectionError as e:
        assert True

    # Check that it fails with an invalid type as input.
    try:
        result = end_g.run([])
        assert False
    except TypeError as e:
        assert True


if __name__ == '__main__':
    test_eg_run()
