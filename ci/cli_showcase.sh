python setup.py install --user

echo '\n\nRun nhlapip without any arguments:\n'
python -m nhlapip

echo '\n\nRun nhlapip for 1 player:\n'
python -m nhlapip Player 8451101

echo '\n\nRun nhlapip for 2 players:\n'
python -m nhlapip Player 8451101 8451102

echo '\n\nRun nhlapip for PlayTypesMd :\n'
python -m nhlapip PlayTypesMd

echo '\n\nRun nhlapip for Awards :\n'
python -m nhlapip Awards

echo '\n\nRun nhlapip for Stanley Cup :\n'
python -m nhlapip Awards 1

echo '\n\nRun nhlapip for Teams :\n'
python -m nhlapip Team

echo '\n\nRun nhlapip for 1 Team :\n'
python -m nhlapip Team 1

echo '\n\nRun nhlapip for 2 Teams :\n'
python -m nhlapip Team 1 2
