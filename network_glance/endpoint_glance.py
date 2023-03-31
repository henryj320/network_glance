"""Module to return whether given endpoints are currently online."""
import requests


def run(endpoints: tuple) -> dict:
    """Return the status of any endpoint.

    Args:
        endpoints (tuple): A tuple containing 1+ endpoints to check.

    Returns:
        dict: A dict containing the status of each endpoint given.
    """
    if not isinstance(endpoints, tuple):
        raise TypeError

    # Sends a GET request to each endpoint given.
    responses = []
    for endpoint in endpoints:
        response = requests.get(endpoint)

        if response.status_code == 200:
            online = True
        else:
            online = False

        # Sets the name to the listen path.
        name = endpoint.split("/")
        name = name[len(name) - 1]

        responses.append({
            "name": name,
            "url": endpoint,
            "online": online
        })

    collated = {
        "endpoints": responses
    }

    return collated


if __name__ == '__main__':
    response = run()
