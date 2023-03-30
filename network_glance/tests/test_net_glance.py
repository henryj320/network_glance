"""Testing script for net_glance. Run it with ` tox -e tests `."""
from network_glance import net_glance as net_g
from network_glance import device_glance as dev_g
from network_glance import endpoint_glance as end_g

import json


def test_ng_run():

    # Check that the result is generated properly.
    result = net_g.run("./network_glance/assets/last_online.json")
    assert list(result.keys())[0] == "devices"

    # Check that it fails with an invalid .json file.
    try:
        result = net_g.run("./fake.json")
        assert False
    except FileNotFoundError as e:
        assert True

    # Check that it fails with an empty .json file.
    try:
        result = net_g.run("./network_glance/tests/empty_json.json")
        assert False
    except json.decoder.JSONDecodeError as e:
        assert True


def test_ng_lookup_hostname():
    valid_json_file = "./network_glance/assets/device_map.json"
    invalid_json_file = "./network_glance/assets/fake.json"

    valid_mac = "20:16:b9:90:2e:4b"
    invalid_mac = "00:00:00:00:00:01"

    # Check it returns correct output on valid input.
    result = net_g.lookup_hostname(valid_json_file, valid_mac)
    assert result[0]
    assert result[1] == "henry-windows-gaming-pc"

    # Check it fails with invalid .json file.
    try:
        result = net_g.lookup_hostname(invalid_json_file, valid_mac)
        assert False
    except FileNotFoundError as e:
        assert True

    result = net_g.lookup_hostname(valid_json_file, invalid_mac)
    assert not result[0]
    assert result[1] == "Uknown Device"


def test_ng_upd_last_online():
    valid_json_file = "./network_glance/assets/last_online.json"
    invalid_json_file = "./network_glance/assets/fake.json"

    valid_alias = "henry-windows-gaming-pc"
    invalid_alias = "ABC"

    # Saves current last_online.json for later.
    last_online_file = open(valid_json_file, "r")
    lo_map = json.load(last_online_file)
    last_online_file.close()

    # Check it succeeds with valid inputs.
    result = net_g.update_last_online(valid_json_file, valid_alias)
    assert result

    # Check it fails with invalid path to .json file.
    try:
        result = net_g.update_last_online(invalid_json_file, valid_alias)
        assert False
    except FileNotFoundError as e:
        assert True

    # Check it fails with an invalid alias.
    result = net_g.update_last_online(valid_json_file, invalid_alias)
    assert not result


    # Resets last_online.json to before testing.
    last_online_file = open(valid_json_file, "w")
    json.dump(lo_map, last_online_file, indent=2)
    last_online_file.close()


if __name__ == '__main__':
    test_ng_run()
    test_ng_lookup_hostname()
    test_ng_upd_last_online()
