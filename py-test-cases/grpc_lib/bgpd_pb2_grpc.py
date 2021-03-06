# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_lib.bgpd_pb2 as bgpd__pb2
import grpc_lib.common_pb2 as common__pb2


class BGPStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartService = channel.unary_unary(
                '/BGP/StartService',
                request_serializer=common__pb2.StartRequest.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )
        self.StopService = channel.unary_unary(
                '/BGP/StopService',
                request_serializer=common__pb2.StopRequest.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )
        self.ConfigureService = channel.unary_unary(
                '/BGP/ConfigureService',
                request_serializer=bgpd__pb2.BGPConfigRequest.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )


class BGPServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartService(self, request, context):
        """Start/Stop.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureService(self, request, context):
        """Configure one or more BGP entities.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BGPServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartService': grpc.unary_unary_rpc_method_handler(
                    servicer.StartService,
                    request_deserializer=common__pb2.StartRequest.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
            'StopService': grpc.unary_unary_rpc_method_handler(
                    servicer.StopService,
                    request_deserializer=common__pb2.StopRequest.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
            'ConfigureService': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureService,
                    request_deserializer=bgpd__pb2.BGPConfigRequest.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BGP', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BGP(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BGP/StartService',
            common__pb2.StartRequest.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BGP/StopService',
            common__pb2.StopRequest.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BGP/ConfigureService',
            bgpd__pb2.BGPConfigRequest.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
