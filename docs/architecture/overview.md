# Repository Architecture Overview

This document describes the overall architecture and organization of the MCP Proof of Concept repository.

## Repository Structure

The repository is organized into several key directories:

```
mcp-poc/
├── docs/               # Documentation
├── projects/           # Web apps, apis, etc
├── templates/          # Template resources (currently not in use)
├── Taskfile.yml        # Task management definition files
└── docker-compose.yml  # Container orchestration
```

## Key Directories

### Documentation (`docs/`)

The documentation is built with MkDocs and organized as follows:

- `docs/index.md` - Main documentation home page
- `docs/architecture/` - Architecture documentation including this overview
- `docs/getting-started/` - Guides for getting started with the project

Documentation is served using MkDocs with the Material theme and can be accessed by running `task docs:serve`.

### Projects (`projects/`)

The projects directory contains the actual implementation of the MCP services:
Each project contains its own Dockerfile for containerization.


## Configuration Files

### Taskfiles

The repository uses [go-task](https://taskfile.dev) for automation through several Taskfiles:

- `Taskfile.yml` - Main entry point with core commands
- `Taskfile.docker.yml` - Docker-related commands
- `Taskfile.aws.yml` - AWS deployment commands
- `Taskfile.terraform.yml` - Infrastructure management commands

### Nix Configuration

The repository uses Nix for reproducible development environments:

- `flake.nix` - Defines the development environment
- `flake.lock` - Locks dependencies to specific versions

### Docker Composition

- `docker-compose.yml` - Defines the services and their relationships

## Network Architecture

In Docker, the services communicate over a dedicated Docker network