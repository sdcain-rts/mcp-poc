{
  description = "MCP POC with Nix Flakes";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: {
    devShells.default =
      let
        pkgs = import nixpkgs {
          system = "x86_64-darwin"; # Adjust for your system if needed. For example:
          # - For Linux: "x86_64-linux"
          # - For macOS with M chips: "aarch64-darwin"
          # - For Windows (via WSL or similar): "x86_64-linux"
        };
      in pkgs.mkShell {
        buildInputs = [
          pkgs.python3
          pkgs.docker
          pkgs.direnv
        ];
      };
  };
}