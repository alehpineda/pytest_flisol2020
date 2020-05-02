import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve
from tempfile import gettempdir

import pytest

from ips import (
    ServiceIPRange,
    parse_ipv4_service_ranges,
    get_aws_service_range,
)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", gettempdir())
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH

# write one or more pytest functions below, they need to start with test_
