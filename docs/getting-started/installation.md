# Installation Guide

This guide covers how to set up the MCP PoC project on your development machine.

## Prerequisites

- Git
- MacOS, Linux, or WSL for Windows users
- Basic terminal knowledge

## Developer Environment Setup (Nix + direnv)

This project uses a reproducible environment powered by Nix Flakes. Once installed, you'll have access to all required tools for local development.

### Step 1: Install Nix

Install Nix from the official site:  
[https://nixos.org/download/](https://nixos.org/download/)

For macOS:

```bash
sh <(curl -L https://nixos.org/nix/install)
```

After install, **restart your terminal**.

### Step 2: Install direnv

Follow the [direnv installation guide](https://direnv.net/docs/installation.html) or use your package manager.

For macOS:

```bash
brew install direnv
```

Then add the shell hook:

#### For Zsh (macOS default)

```bash
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
source ~/.zshrc
```

#### For Bash

```bash
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
source ~/.bashrc
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/yourusername/mcp-poc.git
cd mcp-poc
```

### Step 4: Enable the Dev Shell

```bash
direnv allow
```

This will activate the Nix environment via the `.envrc` file. The first time you run this, it might take a while as it downloads all the dependencies.

## Verifying Installation

To verify your installation is working correctly:

```bash
# List all available tasks
task

# Check if mkdocs is available
mkdocs --version
```

## Next Steps

Now that you have installed the project, check out the [Quick Start Guide](quick-start.md) to run the project and see it in action.