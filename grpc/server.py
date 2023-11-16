from concurrent import futures
import logging
import grpc
import schema_pb2
import schema_pb2_grpc
# from worker.tasks import process_video_watermark


class TaskService(schema_pb2_grpc.TaskServiceServicer):
    def unary_task(self, request, context):
        request_params = {
            "video_url": request.video_url,
            "watermark_url": request.watermark_url,
            "x_offset": request.x_offset,
            "y_offset": request.y_offset,
            "email": request.email,
            "current_epoch": request.current_epoch,
        }

        # process_video_watermark.delay(**request_params)

        logging.info("Received request: {}".format(request_params))

        return schema_pb2.Response(unique_id="s3://bucket/output.mp4", status="OK")


def serve():
    PORT = "8080"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    schema_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port("[::]:" + PORT)

    server.start()
    print("Server started, listening on " + PORT)

    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
