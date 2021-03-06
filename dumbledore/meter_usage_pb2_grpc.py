# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import meter_usage_pb2 as meter__usage__pb2


class MeterUsageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListUsages = channel.unary_unary(
                '/meterusage.MeterUsage/ListUsages',
                request_serializer=meter__usage__pb2._.SerializeToString,
                response_deserializer=meter__usage__pb2.Usages.FromString,
                )


class MeterUsageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListUsages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeterUsageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListUsages': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsages,
                    request_deserializer=meter__usage__pb2._.FromString,
                    response_serializer=meter__usage__pb2.Usages.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'meterusage.MeterUsage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeterUsage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListUsages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meterusage.MeterUsage/ListUsages',
            meter__usage__pb2._.SerializeToString,
            meter__usage__pb2.Usages.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
