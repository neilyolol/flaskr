import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

app.config.from_envvar(‘FLASKR_SETTINGS’,silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init

if __name__ == '__main__':
    app.run()

