from __future__ import print_function
import logging
import grpc
import schema_pb2
import schema_pb2_grpc


def run():
    PORT = "8080"
    SERVER_ADDRESS = "localhost:" + PORT

    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = schema_pb2_grpc.TaskServiceStub(channel)

        response = stub.unary_task(
            schema_pb2.VideoTask(
                video_url="s3://bucket/video.mp4",
                watermark_url="s3://bucket/watermark.png",
                x_offset=10,
                y_offset=10,
                email="test@test.com",
                current_epoch=1234567890,
            )
        )

        print("Received response: \n{}".format(response))


if __name__ == "__main__":
    logging.basicConfig()
    run()
