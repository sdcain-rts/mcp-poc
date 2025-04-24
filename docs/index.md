# AI Developer Toolkit

Welcome to the AI Developer Toolkit documentation. This toolkit provides a comprehensive set of tools and templates to accelerate development of production-ready AI applications.

## Core Components

### Nix
**Purpose**: Provides reproducible development environments across all platforms.

Nix ensures that every developer works with identical tool versions and dependencies regardless of their host OS. It eliminates "it works on my machine" problems by creating isolated, deterministic environments.

### direnv
**Purpose**: Automatically activates your development environment when entering the project directory.

direnv works with Nix to load the correct development environment without manual activation. When you `cd` into your project, the environment is automatically loaded with all required tools.

### Taskfile
**Purpose**: Centralizes all project commands in a consistent interface.

Task (or go-task) simplifies project workflows by providing a uniform command interface. These commands can be used in:
- Local development
- CI/CD pipelines
- Documentation
- Team onboarding

All commands are run with `task [command]` regardless of the underlying tool or language.

### MkDocs
**Purpose**: Provides beautiful, searchable documentation that lives with your code.

MkDocs creates documentation sites that are:
- Version-controlled alongside your code
- Easy to update with Markdown
- Searchable and responsive
- Automatically deployable to GitHub Pages or other services

### Docker & Docker Compose
**Purpose**: Creates consistent environments for development and deployment.

Docker containers ensure that:
- Development environments match production
- Dependencies are cleanly isolated
- Services can be easily composed together
- Applications deploy consistently across environments