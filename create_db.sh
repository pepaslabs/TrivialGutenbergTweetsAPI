#!/bin/bash

set -eu -o pipefail

cat ddl.sql | sqlite3 db.sqlite3
