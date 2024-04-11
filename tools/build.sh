# FMAP
# A audio file format that takes in frequency values or notes and turns them into WAV format.
# GitHub: https://www.gitub.com/0x4248/FMAP
# Licence: GNU General Public Licence v3.0
# By: 0x4248

python tools/dependencies_check.py

if [ $? -eq 1 ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install --user --upgrade setuptools
fi

python setup.py sdist bdist_wheel
