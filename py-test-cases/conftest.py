import os
import sys

base_path = os.path.dirname(__file__)
lib_list = [
    '/test-cases/sanity/',
    '/test-cases/fixtures/',
    '/test-cases/utils/',
    '/test-cases/grpc_lib',
]

# Initializing the library paths here.
for path in  lib_list :
    abs_path = base_path + path
    if abs_path not in sys.path :
        print("| %s" %(abs_path))
        sys.path.append(abs_path)

sys.path.append('./')
sys.path.append('../')

# We are using kne to deploy a basis topology.
# Get the path of the kne_cli utility.
abs_path_kne = os.path.abspath(base_path + '/kne.sh')
fd = open(abs_path_kne, "r")
while fd :
    line = fd.readline()
    [envvar, value] = line.split('=')
    if (envvar.lstrip().rstrip() == "KNE_BIN_PATH") :
       os.environ['KNE_BIN_PATH'] = value.lstrip().rstrip()
       break
fd.close()
