VENV_SUBDIR="extract_load/igdb"
VENV_PATH_PARENT="$(git rev-parse --show-toplevel)/$VENV_SUBDIR"
VENV_PATH="$VENV_PATH_PARENT/.venv"

# Make sure .venv is in .gitignore
if grep -q '^.venv$' $VENV_PATH_PARENT/.gitignore; then
  echo "Virtual environment already in $VENV_PATH_PARENT/.gitignore"
else
  echo '.venv' >> "$VENV_PATH_PARENT/.gitignore"
fi

# Set platform-specific subdir (handles if running this on Windows)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    VENV_ACTIVATE_SUBDIR="Scripts"
else
    VENV_ACTIVATE_SUBDIR="bin"
fi

# Create virtual environment & activate it
python3 -m venv $VENV_PATH
source $VENV_PATH/$VENV_ACTIVATE_SUBDIR/activate
python3 -m pip install --upgrade pip
pip install -r "$VENV_PATH_PARENT/requirements.txt"
