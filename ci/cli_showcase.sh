python setup.py install

echo '\n\nGet nhlapip usage and examples:\n'
nhlapip

echo '\n\nGet data from NHLAPI for 1 player:\n'
nhlapip Player 8451101

echo '\n\nGet data from NHLAPI for 2 players:\n'
nhlapip Player 8451101 8451102

echo '\n\nGet data from NHLAPI for PlayTypesMd :\n'
nhlapip PlayTypesMd

echo '\n\nGet data from NHLAPI for Awards :\n'
nhlapip Awards

echo '\n\nGet data from NHLAPI for Stanley Cup :\n'
nhlapip Awards 1

echo '\n\nGet data from NHLAPI for Teams :\n'
nhlapip Team

echo '\n\nGet data from NHLAPI for 1 Team :\n'
nhlapip Team 1

echo '\n\nGet data from NHLAPI for 2 Teams :\n'
nhlapip Team 1 2

echo '\n\nGet data from NHLAPI for current playoffs :\n'
nhlapip Tournament playoffs

echo '\n\nGet data from NHLAPI for current olympics :\n'
nhlapip Tournament olympics

echo '\n\nGet data from NHLAPI for season schedule :\n'
nhlapip Schedule 19931994

echo '\n\nGet data from NHLAPI for season stadings :\n'
nhlapip Standings 19931994
