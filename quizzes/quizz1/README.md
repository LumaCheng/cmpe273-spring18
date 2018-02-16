
Required Packages

python3
grpc
IDE: visual studio code
extensions: vscode-proto3

# Install grpc tools

```sh
pip install grpcio-tools
```

# Compile the proto file

```sh
python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. ping.proto 
```# cmpe273-spring18