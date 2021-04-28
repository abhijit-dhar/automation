import os

def pytest_addoption(parser):
    parser.addoption(
        "--config", 
        action="store", 
        default="../test_bed_setup/2node-ixia.pb.txt")


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.config
    if 'config' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("config", [option_value])
