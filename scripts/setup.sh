find . -maxdepth 2 -type f -name '.example.env' -exec sh -c 'cp "$1" "${1%/*}/.env"' _ {} \;
