#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('articles.db')

conn.execute("""
	CREATE TABLE ARTICLES (
		id INTEGER NOT NULL,
		title CHARACTER,
		docreation CHARACTER,
		articlecategory INTEGER,
		CONSTRAINT PK_articles PRIMARY KEY (id))""")



conn.commit()