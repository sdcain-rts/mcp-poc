# 🧪 Developer Environment Setup (Nix + direnv)

This project uses a reproducible environment powered by **Nix Flakes**. Once installed, you'll have access to all required tools for local development.

---

## ✅ Step 1: Install Nix

Install Nix from the official site:  
🔗 https://nixos.org/download/

For macOS:

    sh <(curl -L https://nixos.org/nix/install)

> After install, **restart your terminal**.

---

## ✅ Step 2: Install `direnv`

🔗 https://direnv.net/docs/installation.html

    brew install direnv

Then add the shell hook:

### For Zsh (macOS default)

    echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
    source ~/.zshrc

---

## ✅ Step 3: Enable the Dev Shell

From the project root:

    direnv allow

This will activate the Nix environment via the `.envrc` file.

---

# MCP PoC

This repo contains the following projects:

- **MCP Client (Python)**: A FastAPI app that uses LangGraph and OpenAI to call MCP tools.
- **MCP Server (Python)**: A FastAPI app exposing MCP tools using the modelcontext SDK.
- **MCP Server (NestJS)**: A NestJS app exposing additional MCP tools.

## Folder Structure

```
├── docker-compose.yml
├── flake.lock
├── flake.nix
├── .envrc
├── .env
├── README.md
├── projects
│   ├── mcp-client-python
│   ├── mcp-server-python
│   └── mcp-server-nestjs
```

## Build and Run Instructions

1. Build and start all services:
   ```bash
   docker-compose up --build
   ```

2. Access the services:
   - MCP Client: [http://localhost:8001](http://localhost:8001)
   - Python MCP Server: [http://localhost:8000](http://localhost:8000)
   - NestJS MCP Server: [http://localhost:3000](http://localhost:3000)

3. Stop the services:
   ```bash
   docker-compose down
   ```