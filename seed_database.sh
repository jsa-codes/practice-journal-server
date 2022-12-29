#!/bin/bash

rm db.sqlite3
rm -rf ./practicejournalapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations practicejournalapi
python3 manage.py migrate practicejournalapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata instructors
python3 manage.py loaddata students
python3 manage.py loaddata audio
python3 manage.py loaddata journalentries
python3 manage.py loaddata comments