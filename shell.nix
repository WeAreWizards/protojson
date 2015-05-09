# <nixpkgs> is the latest unstable channel (30th April ATM).
# call:
#  nix-shell --pure
#  pip freeze > requirements.txt
with import <nixpkgs> {};
buildPythonPackage rec {
  srcs = ./.;
  name = "";
  propagatedBuildInputs = with pythonPackages; [
    pip
    flask
    protobuf
  ];
}
