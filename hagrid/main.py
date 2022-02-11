import grpc
import meter_usage_pb2
import meter_usage_pb2_grpc
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.protobuf.json_format import MessageToDict


def get_usage_data():
    channel = grpc.insecure_channel('localhost:50051')
    stub = meter_usage_pb2_grpc.MeterUsageStub(channel)
    response = stub.ListUsages(meter_usage_pb2.Usage())
    return response


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/usages/")
def read_root():
    data = get_usage_data()
    serialized_data = MessageToDict(data)
    return {
        'data': serialized_data['usage']
    }

