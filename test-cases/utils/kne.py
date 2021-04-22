import os
import pytest
def kne_execute(kne, command, filename) :
    cmd_string = kne + ' ' + command + ' ' + filename
    print(cmd_string)
    try:
        retval = os.system(cmd_string)
    except :
        pytest.fail("unable to execute the command %s" %(cmd_string)) 
    return retval

