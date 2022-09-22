# Get the script filename
old=$(basename $(readlink -nf $0))

# Remove the extension
old=${old%.sh}

# Assume the filename is a number and increment it
new=$((old + 1))

# Rename the script
mv $0 "$new.sh"