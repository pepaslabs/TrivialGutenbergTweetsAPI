#!/bin/bash

set -e -o pipefail

cat ddl.sql | sqlite3 db.sqlite3
