# Task Runner

The MCP PoC project uses [go-task](https://taskfile.dev) for development automation. The tasks are organized in a modular structure to keep them organized by domain.

## Task Structure

The task files are organized as follows:

- `Taskfile.yml` - Main entrypoint with common tasks
- `Taskfile.docker.yml` - Docker-related tasks
- `Taskfile.aws.yml` - AWS deployment tasks
- `Taskfile.terraform.yml` - Infrastructure as code tasks

## Common Tasks

### Getting Started

```bash
# List all available tasks
task

# Set up the development environment
task dev:setup
```

### Docker Operations

```bash
# Build all services
task build:all

# Run all services in detached mode
task run:all

# Stop all services
task stop:all

# View logs from all services
task docker:logs
```

### Docker-Specific Tasks

```bash
# Build Docker containers
task docker:build

# Start containers in detached mode
task docker:up

# View container logs
task docker:logs

# Stop all containers
task docker:down

# List running containers
task docker:ps

# Build a specific service
task docker:client:build  # Build only the MCP client
task docker:server-py:build  # Build only the Python MCP server
```

### AWS Tasks

```bash
# Configure AWS CLI
task aws:configure

# Create ECR repositories
task aws:create:ecr-repos

# Deploy images to ECR
task aws:deploy:images
```

### Terraform Tasks

```bash
# Initialize Terraform
task terraform:init

# Create execution plan
task terraform:plan

# Apply changes
task terraform:apply

# Destroy infrastructure
task terraform:destroy
```

## Adding New Tasks

To add new tasks:

1. Identify which domain file the task belongs in
2. Add the task to the appropriate file
3. For cross-domain tasks, use the main `Taskfile.yml` and create dependencies

Example of adding a new task to `Taskfile.docker.yml`:

```yaml
prune:
  desc: Remove all unused Docker resources
  cmds:
    - docker system prune -f
```

## Running Tasks with Variables

Some tasks accept variables that can be provided on the command line:

```bash
# Select a specific Terraform workspace
task terraform:workspace:select -- dev

# Tag and push a specific Docker image
task aws:tag-and-push -- my-custom-image
```