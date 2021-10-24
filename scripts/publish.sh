./scripts/clean.sh

# Build project
python3 setup.py bdist_wheel
twine upload dist/*
