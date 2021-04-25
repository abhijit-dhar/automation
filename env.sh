#------------------------------------------------------------------------------
# Export KNE cli path.
#------------------------------------------------------------------------------ 
PWD=`pwd`
KNE_BIN_PATH='/home/ixia/kne/kne_cli/kne_cli'

PYTHONPATH="$PYTHONPATH:$PWD/test-cases/"
PYTHONPATH="$PYTHONPATH:$PWD/test-cases/grpc_lib"
PYTHONPATH="$PYTHONPATH:$PWD/test-cases/bgp_lib"
PYTHONPATH="$PYTHONPATH:./:../"

export KNE_BIN_PATH
export PYTHONPATH
