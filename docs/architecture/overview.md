# Architecture Overview

The Model Context Protocol (MCP) Proof of Concept demonstrates how AI models can interact with external tools provided by different services.

## High-Level Architecture

The project consists of three main components:

1. **MCP Client** - A FastAPI service that processes user messages using LangGraph and OpenAI.
2. **MCP Python Server** - A FastAPI service exposing tools via the Model Context Protocol.
3. **MCP NestJS Server** - A NestJS service exposing additional tools.

```
┌─────────────┐     ┌─────────────────┐     ┌──────────────┐
│             │     │                 │     │              │
│    User     │────▶│   MCP Client    │────▶│  OpenAI API  │
│             │     │   (FastAPI)     │     │              │
└─────────────┘     └────────┬────────┘     └──────────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │                             │
              │      MCP Protocol Layer     │
              │                             │
              └───────────┬─────────┬───────┘
                          │         │
              ┌───────────▼─┐     ┌─▼───────────┐
              │             │     │             │
              │ MCP Python  │     │ MCP NestJS  │
              │   Server    │     │   Server    │
              │             │     │             │
              └─────────────┘     └─────────────┘
```

## Flow of Information

1. The user sends a message to the client API.
2. The client processes the message using a LangGraph agent and OpenAI.
3. If the model decides to use tools, requests are sent to the appropriate MCP server.
4. The MCP servers execute the tools and return results.
5. Results are fed back to the model for further processing.
6. A final response is returned to the user.

## Key Components

### MCP Client

- Built with FastAPI and LangGraph
- Manages conversation state
- Routes tool calls to appropriate MCP servers
- Communicates with OpenAI API

### MCP Python Server

- Built with FastAPI and the modelcontext SDK
- Exposes tools related to orders and inventory
- Implements the Model Context Protocol for standardized tool access

### MCP NestJS Server

- Built with NestJS
- Provides additional tools in a TypeScript/JavaScript environment
- Demonstrates cross-language interoperability

## Network Architecture

In Docker, the services communicate over a dedicated Docker network:

- MCP Client Python: Port 8001
- MCP Server Python: Port 8000
- MCP Server NestJS: Port 3000

## Next Steps

- Learn more about the [Components](components.md) in detail
- Understand the [MCP Protocol](mcp-protocol.md) specification