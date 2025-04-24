# Getting Started with the AI Developer Toolkit

Once you've completed the installation steps in the README, you're ready to start using the toolkit. This guide introduces you to Taskfile, the core workflow tool that powers the AI Developer Toolkit.

## Understanding Taskfile

Taskfile is a task runner and build tool that serves as the command center for all toolkit operations. Think of Taskfile as a simplified, modern alternative to Make that works consistently across all platforms.

### Why Taskfile?

Taskfile centralizes all commands in your development workflow, providing several benefits:

1. **Consistent Interface**: All commands follow the same pattern: `task [command]`
2. **Self-documenting**: Running `task` shows all available commands with descriptions
3. **Cross-platform**: Works identically on macOS, Linux, and Windows
4. **Composable**: Tasks can depend on other tasks
5. **Reusable**: The same commands work in documentation, CI/CD pipelines, and local development

### Taskfile Structure

The AI Developer Toolkit uses a modular Taskfile structure:

- `Taskfile.yml` - The main entry point with core commands
- `Taskfile.docker.yml` - Docker-related commands
- `Taskfile.aws.yml` - AWS deployment commands
- `Taskfile.terraform.yml` - Infrastructure management commands

## Common Tasks

Here are some essential tasks to get started:

### Documentation

```bash
# Serve documentation locally (opens in browser)
task docs:serve

# Build documentation site
task docs:build
```

### Creating New AI Projects

```bash
# Create a frontend project (React, Next.js, Vue, Angular)
task frontend:create:react

# Create a backend project (FastAPI, NestJS, Spring, Express)
task backend:create:fastapi

# Set up database with Liquibase
task db:create:postgres
task db:liquibase:init

# Create cloud infrastructure templates
task infra:create:aws
```

### Running Services

```bash
# Build all services
task build:all

# Start all services
task run:all

# Stop all services
task stop:all
```

## Task Structure

Each task follows a standard structure in the YAML files:

```yaml
task-name:
  desc: Description of what the task does
  cmds:
    - command to run
    - another command to run
  deps:
    - dependency-task
```

## Creating Your First AI Project

Let's walk through creating a simple AI project using the toolkit:

1. **Create a new frontend**: 
   ```bash
   task frontend:create:react -- my-ai-app
   ```

2. **Add a backend API**:
   ```bash
   task backend:create:fastapi -- my-ai-api
   ```

3. **Set up a database with Liquibase**:
   ```bash
   task db:create:postgres -- my-ai-app
   task db:liquibase:init -- my-ai-app
   ```

4. **Create infrastructure templates**:
   ```bash
   task infra:create:aws -- my-ai-app
   ```

5. **Run the application locally**:
   ```bash
   cd my-ai-app
   task run:all
   ```

## Next Steps

Now that you understand the basics of using Taskfile with the AI Developer Toolkit, explore these specific components:

- [Frontend Templates](../toolkit/frontend-templates.md) - Ready-to-use frontend frameworks
- [Backend Templates](../toolkit/backend-templates.md) - API servers pre-configured for AI
- [Database Management](../toolkit/database-management.md) - Database tools and migrations
- [Infrastructure](../toolkit/infrastructure.md) - Deployment templates