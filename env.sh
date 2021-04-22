#------------------------------------------------------------------------------
# Export KNE cli path.
#------------------------------------------------------------------------------ 
PWD=`pwd`
export KNE_BIN_PATH='/home/ixia/kne/kne_cli/kne_cli'
export PYTHONPATH="$PYTHONPATH:$PWD/test-cases/:$PWD/test-cases/grpc_lib:./:../" 
