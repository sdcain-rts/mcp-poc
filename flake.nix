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
            docker
            direnv
          ];

          shellHook = ''
          '';
        };
      });
}