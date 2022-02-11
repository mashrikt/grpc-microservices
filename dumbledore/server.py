from concurrent import futures
import logging
import csv

import grpc
import meter_usage_pb2
import meter_usage_pb2_grpc


class MeterUsage(meter_usage_pb2_grpc.MeterUsage):

    def ListUsages(self, request, context):
        response_data = []
        with open('meterusage.csv', 'r') as read_obj:
            next(read_obj)
            csv_reader = csv.reader(read_obj)
            for c in csv_reader:
                response_data.append(meter_usage_pb2.Usage(
                    time=c[0],
                    quantity=float(c[1])
                ))
        return meter_usage_pb2.Usages(usage=response_data)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meter_usage_pb2_grpc.add_MeterUsageServicer_to_server(MeterUsage(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
