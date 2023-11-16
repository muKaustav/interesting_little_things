FROM grpc/python

WORKDIR /app

RUN pip install --no-cache-dir -r grpc_requirements.txt

COPY . .

EXPOSE 50051

CMD ["python", "grpc.py"]
