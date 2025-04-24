{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";  # Use the latest unstable Nix packages
    flake-utils.url = "github:numtide/flake-utils";  # Utility functions for easier flake setup
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;  # Allow unfree (proprietary) packages if needed
      };
    in
      with pkgs; {
        devShells.default = mkShell {
          buildInputs = [
            python3
            python3Packages.pip
            python3Packages.mkdocs
            python3Packages.mkdocs-material  # Adding Material theme for mkdocs
            python3Packages.pymdown-extensions  # Common markdown extensions
            # Testing dependencies
            python3Packages.pytest
            python3Packages.pytest-asyncio
            python3Packages.httpx
            python3Packages.pytest-cov
            docker
            direnv
            go-task
          ];

          shellHook = ''
            export PYTHONPATH="$PWD/projects/mcp-server-python:$PYTHONPATH"
          '';
        };
      });
}