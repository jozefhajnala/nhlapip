pip install pytest
pip install coverage

python setup.py install --user
python setup.py test

python -m coverage run -m pytest
python -m coverage report