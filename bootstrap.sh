#!/usr/bin/env bash

set -e
set -x

rm -f db.sqlite3
./create_db.sh
./fetch_books.sh
./populate_db.py

