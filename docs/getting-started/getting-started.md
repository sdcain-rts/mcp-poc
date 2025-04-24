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

## Next Steps

Now that you understand the basics of using Taskfile with the MCP project, explore these specific aspects:

- [Architecture Overview](../architecture/overview.md) - Understand how MCP components work together
- [Task Runner](../development-guides/task-runner.md) - Learn more about task management
- [Contributing](../development-guides/contributing.md) - Guidelines for contributing to the project