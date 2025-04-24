# MCP PoC (Model Context Protocol Proof of Concept)

This project demonstrates a working implementation of the Model Context Protocol, enabling AI models to effectively use tools and contextual information provided by separate services.

## Quick Setup

### 1. Install Nix

<details>
<summary><b>macOS</b></summary>

```bash
sh <(curl -L https://nixos.org/nix/install)
```
After installation, restart your terminal or run:
```bash
. ~/.nix-profile/etc/profile.d/nix.sh
```
</details>

<details>
<summary><b>Linux</b></summary>

```bash
sh <(curl -L https://nixos.org/nix/install) --daemon
```
After installation, restart your terminal or run:
```bash
. ~/.nix-profile/etc/profile.d/nix.sh
```
</details>

<details>
<summary><b>Windows (WSL2)</b></summary>

First, ensure WSL2 is installed and you have a Linux distribution like Ubuntu.

Then, inside your WSL2 environment:
```bash
sh <(curl -L https://nixos.org/nix/install)
```
After installation, restart your terminal or run:
```bash
. ~/.nix-profile/etc/profile.d/nix.sh
```
</details>

### 2. Install direnv

<details>
<summary><b>macOS</b></summary>

```bash
brew install direnv
```

Add to your shell configuration:
- **For Zsh (default):**
  ```bash
  echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
  source ~/.zshrc
  ```
- **For Bash:**
  ```bash
  echo 'eval "$(direnv hook bash)"' >> ~/.bash_profile
  source ~/.bash_profile
  ```
</details>

<details>
<summary><b>Linux</b></summary>

Using package manager:
```bash
# For Ubuntu/Debian
sudo apt-get update && sudo apt-get install direnv

# For Fedora
sudo dnf install direnv

# For Arch Linux
sudo pacman -S direnv
```

Then add to your shell configuration:
- **For Bash:**
  ```bash
  echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
  source ~/.bashrc
  ```
- **For Zsh:**
  ```bash
  echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
  source ~/.zshrc
  ```
</details>

<details>
<summary><b>Windows (WSL2)</b></summary>

Inside your WSL2 Linux distribution:
```bash
# For Ubuntu/Debian
sudo apt-get update && sudo apt-get install direnv
```

Then add to your shell configuration:
```bash
# If using Bash
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
source ~/.bashrc

# If using Zsh
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
source ~/.zshrc
```
</details>

### 3. Enable Development Environment

```bash
direnv allow
```

The first time you run this, it may take several minutes as Nix downloads and sets up all the required dependencies.

### 4. Run Documentation

Start the documentation server:

```bash
task docs:serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to explore the complete project documentation.