# Backend Templates

The AI Developer Toolkit includes several backend templates pre-configured for AI development. Each template provides a solid foundation with AI libraries already integrated, API endpoints set up, and development tooling preconfigured.

## Available Templates

### FastAPI + LangGraph (Python)

A Python-based backend with FastAPI and LangGraph for orchestrating complex AI workflows.

**Features:**
- FastAPI framework with async support
- LangGraph for multi-step AI workflows
- OpenAI, Anthropic, and local model integrations
- API documentation with Swagger UI
- Environment variable management
- Structured logging
- Unit and integration testing setup
- Docker configuration

**Usage:**
```bash
task backend:create:fastapi -- my-ai-backend
```

### NestJS + LangChain.js (TypeScript)

A TypeScript backend built with NestJS and LangChain.js for enterprise-grade AI applications.

**Features:**
- NestJS framework with dependency injection
- LangChain.js for composable AI capabilities
- Module-based architecture
- OpenAI, Anthropic SDK integrations
- Response streaming for LLM outputs
- Authentication and authorization
- Swagger API documentation
- Unit and e2e testing
- Docker configuration

**Usage:**
```bash
task backend:create:nestjs -- my-ai-backend
```

### Spring Boot + LangChain4j (Java)

A Java-based backend built with Spring Boot and LangChain4j for enterprise Java environments.

**Features:**
- Spring Boot framework
- LangChain4j for Java-based LLM orchestration
- OpenAI, Anthropic integrations
- RESTful API design
- Response streaming
- Authentication and authorization
- API documentation with SpringDoc
- Testing with JUnit and Mockito
- Docker configuration

**Usage:**
```bash
task backend:create:spring -- my-ai-backend
```

### Express + OpenAI SDK (Node.js)

A lightweight Node.js backend with Express and OpenAI SDK.

**Features:**
- Express.js framework
- OpenAI SDK integration
- RESTful API design
- Environment configuration
- Middleware for authentication
- Error handling
- Basic testing setup
- Docker configuration

**Usage:**
```bash
task backend:create:express -- my-ai-backend
```

## AI Capabilities

All backend templates include:

- LLM integration (OpenAI, Anthropic, etc.)
- Tool use and function calling
- Context management
- Response streaming
- Error handling for AI-specific issues
- Prompt management

## Customizing Templates

You can customize backend templates during creation:

```bash
task backend:create:fastapi -- my-ai-backend --database=postgres --auth=jwt --ai-provider=openai
```

## Extending Templates

All templates are designed to be extended with additional features. Check the [Extending Templates](../development-guides/extending-templates.md) guide for more information.