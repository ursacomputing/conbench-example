import subprocess


def get_cli_output(command):
    result = subprocess.run(command, capture_output=True, check=True)
    return result.stdout.decode("utf-8").strip().replace("\x08", "")


def assert_cli(command, expected):
    actual = get_cli_output(command)
    assert actual == expected.strip()
