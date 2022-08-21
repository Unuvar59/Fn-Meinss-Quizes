Furkan Unuvar
150200334

## For firebase package:
###### Way 1: -if you have "git"-
    pip install git+https://github.com/ozgur/python-firebase 
###### Way 2:
    pip install python-firebase
    -Open package source, (python\site-packages\firebase)
    -Renamed async.py as async_.py, save
    -open __init__.py, changed .async as .async_ in line 3. Save and close
    -open firebase.py, changed .async as .async_ in line 12. Save and close

## For requests package:
    pip install requests

Run term_project.py and enjoy!