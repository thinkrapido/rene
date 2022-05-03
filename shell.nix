{ pkgs ? import <nixpkgs> {} }:
let 
    myAppEnv = pkgs.poetry2nix.mkPoetryEnv {
        projectDir = ./.;
        editablePackageSources = {
            rene = ./rene;
        };
    };
in myAppEnv.env.overrideAttrs (oldAttrs: {
    buildInputs = with pkgs ; [
	    python310
        direnv
        poetry
        fuse
        python310.pkgs.pandas
    ];
    nativeBuildInputs = with pkgs ; [
        python310.pkgs.flit-core
        ccache
    ];
    LD_LIBRARY_PATH="${pkgs.fuse}/lib";
    PROJECT_ROOT = builtins.toString ./.;
})
