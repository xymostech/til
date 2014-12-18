#!/usr/bin/env bash

set -e

rm db.sqlite

sqlite3 db.sqlite "CREATE TABLE users (
    userid INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);"
sqlite3 db.sqlite "CREATE TABLE posts (
    postid INTEGER PRIMARY KEY,
    time INTEGER,
    post TEXT,
    creator INTEGER,
    FOREIGN KEY(creator) REFERENCES users(userid)
);"

sqlite3 db.sqlite "INSERT INTO users VALUES (NULL, 'emily', 'pass');"
