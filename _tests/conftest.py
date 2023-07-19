import subprocess
import time
from http.client import HTTPConnection
from pathlib import Path

import pytest


def http_server_process(directory: str) -> subprocess.Popen:
    """
    Call python's http.server module as a child process, wait for initialization and yield server for tests.
    """

    server = subprocess.Popen(['python3', '-m', 'http.server', '--directory', directory],
                              encoding='utf-8',
                              universal_newlines=True)

    retries = 5
    while retries > 0:
        conn = HTTPConnection('localhost:8000')
        try:
            conn.request('HEAD', '/')
            response = conn.getresponse()
            if response is not None:
                return server
        except ConnectionRefusedError:
            time.sleep(0.5)
            retries -= 1

    raise RuntimeError('Failed to start http server')


@pytest.fixture(scope='session')
def path_to_site():
    return Path(__file__).parent.parent.joinpath('_test_site').absolute()

@pytest.fixture(scope='session')
def path_to_source():
    return Path(__file__).parent.parent.absolute()


@pytest.fixture(scope='session')
def bumblebuild(path_to_site: Path, path_to_source:Path):
    result = subprocess.run(['bundle', 'exec', 'jekyll', 'build', '-d', path_to_site],
                            capture_output=True, text=True, cwd=path_to_source)
    assert 'done in' in result.stdout


@pytest.fixture(scope='session')
def bumbleserve(path_to_site, bumblebuild):
    class Server:
        def __init__(self):
            self.host = 'localhost'
            self.port = 8000

    server_process = http_server_process(path_to_site)
    yield Server()

    server_process.terminate()
    server_process.wait()
