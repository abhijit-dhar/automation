#------------------------------------------------------------------------------
# Export python path
#------------------------------------------------------------------------------
alias python=python3
PWD=`pwd`
source ./kne.sh
PYTHONPATH="$PYTHONPATH:$PWD/test-cases/"
PYTHONPATH="$PYTHONPATH:$PWD/test-cases/grpc_lib"
PYTHONPATH="$PYTHONPATH:$PWD/test-cases/bgp_lib"
PYTHONPATH="$PYTHONPATH:./:../"
export PYTHONPATH
