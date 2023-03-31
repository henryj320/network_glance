"""Testing script for net_glance. Run it with ` tox -e tests `."""
from network_glance import net_glance as net_g
from network_glance import device_glance as dev_g
from network_glance import endpoint_glance as end_g

import datetime
import json

valid_network = {
    'devices': [
        {
            'name': 'home-router',
            'ip': '192.168.1.1',
            'mac': '10:47:38:62:9a:90'
        },
        {
            'name': 'henry-android-phone',
            'ip': '192.168.1.100',
            'mac': '96:1a:29:79:b9:62'
        },
        {
            'name': 'henry-windows-gaming-pc',
            'ip': '192.168.1.103',
            'mac': '20:16:b9:90:2e:4b'
        }
    ]
}

valid_devices = [
    "henry-windows-gaming-pc",
    "henry-android-phone",
    "henry-armbian-rpi-4-model-b"
]


def test_dg_run():

    # Check it succeeds with correct inputs.
    result = dev_g.run(valid_network, valid_devices)
    assert len(result["personal_devices"]) > 0

    # Check it fails if devices is a number.
    try:
        result = dev_g.run(valid_network, 123)
        assert False
    except TypeError as e:
        assert True

    # Check it fails if network is wrong.
    try:
        result = dev_g.run({}, valid_devices)
        assert False
    except KeyError as e:
        assert True


def test_dg_get_last_on():

    valid_json_file = "./network_glance/tests/test_last_online.json"
    invalid_json_file = "./network_glance/assets/fake.json"

    valid_alias = "test"
    invalid_alias = "ABC"

    current_time = datetime.datetime.now()
    date = str(current_time).split(" ")[0]

    # Saves current last_online.json for later.
    last_online_file = open(valid_json_file, "r")
    lo_map = json.load(last_online_file)
    last_online_file.close()

    # Check that it passes with online = False
    result = dev_g.get_last_online(valid_json_file, False, valid_alias)
    result_date = str(result).split(" ")[0]
    assert result_date == "2016-01-02"

    # Check that it passes with valid inputs.
    result = dev_g.get_last_online(valid_json_file, True, valid_alias)
    result_date = str(result).split(" ")[0]
    assert date == result_date

    # Check that it fails with invalid .json file.
    try:
        result = dev_g.get_last_online(invalid_json_file, True, valid_alias)
        assert False
    except FileNotFoundError as e:
        assert True

    # Resets last_online.json to before testing.
    last_online_file = open(valid_json_file, "w")
    json.dump(lo_map, last_online_file, indent=2)
    last_online_file.close()

    # Check that it returns None if alias is invalid.
    result = dev_g.get_last_online(valid_json_file, True, invalid_alias)
    assert result is None
    result = dev_g.get_last_online(valid_json_file, False, invalid_alias)
    assert result is None


if __name__ == '__main__':
    test_dg_run()
    test_dg_get_last_on()
