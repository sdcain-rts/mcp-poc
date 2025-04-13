# 🧪 Developer Environment Setup (Nix + direnv)

This project uses a reproducible environment powered by **Nix Flakes**. Once installed, you'll have access to all required tools for local development and Kubernetes workflows.

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

# MCP Monorepo

This monorepo contains the following projects:

- **MCP Client (Python)**: A FastAPI app that uses LangGraph and OpenAI to call MCP tools.
- **MCP Server (Python)**: A FastAPI app exposing MCP tools using the modelcontext SDK.
- **MCP Server (NestJS)**: A NestJS app exposing additional MCP tools.

## Folder Structure

```
/Users/shawncain/Documents/repos/mcp-poc
├── docker-compose.yml
├── .env
├── README.md
├── projects
│   ├── mcp-client-python
│   ├── mcp-server-python
│   └── mcp-server-nestjs
```

## Installing UV

To manage dependencies for the MCP projects, we use UV. Follow the instructions below to install UV on your operating system:

### macOS
1. Open a terminal.
2. Run the following command to install UV:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

### Linux
1. Open a terminal.
2. Run the following command to install UV:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

### Windows
1. Open PowerShell as Administrator.
2. Run the following command to install UV:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

Once UV is installed, you can navigate to each project directory and run `uv install` to set up the dependencies.

## Using pipx for Dependency Management

To manage Python dependencies for the MCP projects, we recommend using `pipx`. It isolates installations in their own virtual environments, ensuring a clean and manageable setup.

### Installing pipx
1. Install pipx using Homebrew:
   ```bash
   brew install pipx
   pipx ensurepath
   ```

2. Verify the installation:
   ```bash
   pipx --version
   ```

### Installing Project Dependencies
1. Navigate to the project directory (e.g., `mcp-client-python`):
   ```bash
   cd projects/mcp-client-python
   ```

2. Use pipx to install dependencies:
   ```bash
   pipx install -r requirements.txt
   ```

3. Repeat the process for the `mcp-server-python` project:
   ```bash
   cd ../mcp-server-python
   pipx install -r requirements.txt
   ```

### Notes
- If you encounter any issues, ensure that `pipx` is added to your PATH by running `pipx ensurepath` again.

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