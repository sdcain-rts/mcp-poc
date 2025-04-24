# Quick Start Guide

This guide will help you get the MCP PoC up and running quickly.

## Prerequisites

Ensure you've completed the [Installation](installation.md) process first.

## Starting the Services

The easiest way to run all services is using the task runner:

```bash
# Build and start all services in Docker
task run:all
```

This command will:
1. Build all Docker containers
2. Start the services in detached mode
3. Create a network for the services to communicate

## Accessing the Services

Once running, you can access the services at:

- MCP Client: [http://localhost:8001](http://localhost:8001)
- Python MCP Server: [http://localhost:8000](http://localhost:8000)
- NestJS MCP Server: [http://localhost:3000](http://localhost:3000)

## Testing the API

You can test the chat API with a simple curl command:

```bash
curl -X POST http://localhost:8001/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, can you help me find information about orders?", "conversation_id": "test-1"}'
```

## Viewing Logs

To see the logs from all services:

```bash
task docker:logs
```

## Stopping the Services

When you're done, you can stop all services with:

```bash
task stop:all
```

## Next Steps

Now that you've got the project running, explore:

- [Architecture Overview](../architecture/overview.md) to understand how it works
- [User Guide](../user-guides/using-client.md) to learn how to use the MCP Client
- [Development Guide](../development-guides/environment-setup.md) if you want to contribute