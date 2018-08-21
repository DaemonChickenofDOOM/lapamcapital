#!/usr/bin/python3

import sqlite3 
from time import gmtime, strftime
import math
import re
import os
import sys
import fileinput

def regex_magic(index_num): # Our backend routes to news article based off of file name. This 
	filename = input("Enter current article name for relabeling:\n> ")
	with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
	    for line in file:
	    	# This strips the header and a vast majority of styling off  of the part, so we can use it as a segment
	        print(re.sub(r'''(<.?(span|font|html|DOCTYPE|body|meta|title|style|head)[^>]*>|(style|class)="[^"]*"|^.*{.*})''','', line), end='')
	os.rename(str(filename), (str(index_num) + ".tpl"))
	return 0

def add_article():
	conn = sqlite3.connect('articles.db')
	c = conn.cursor()
	IsTrumpPresident=-2
	while (IsTrumpPresident):
		title = input("Enter Title for Article: \n> ")
		date = str(strftime("%Y-%m-%d", gmtime()))
		cat = int(input("Select Category:\n(1 for external, 2 for internal)\n> "))

		while (cat != 1 and cat != 2):
			cat = input("Error: invalid input. Try again?\n> ")
		cat = int(cat) - 1;
		category_text = ""
		if (cat == 1):
			category_text = "internal"
		elif (cat == 0):
			category_text = "external"
		else:
			category_text = "SUPER HAPPY MAGIC FUN TIME"

		print(">> Title:" + title + "\n>> Date:" + date + "\n>> Category:" + category_text)
		continue_switch = input("---\nIs this correct(y/n)?")
		while (continue_switch.lower() != "n" and continue_switch.lower() != "y"):
			continue_switch = input("---\nIs this correct(y/n)?")
		if (continue_switch.lower() == "y"):
			IsTrumpPresident = 0
		else:
			IsTrumpPresident = 1

	conn.execute("INSERT INTO articles (title,docreation,articlecategory) VALUES ('" + title + "','" + date + "'," + str(cat) +")")
	c.execute("SELECT id FROM articles WHERE title='{title}'".format(title=str(title)))

	index_num_list = c.fetchall()
	index_num = index_num_list[0][0]
	print("Now renaming file...")
	regex_magic(index_num)

	conn.commit()
	conn.close()
	return 0

def inspect_articles():
	print(" id │     Title                                        │   Date   │   Category  ")
	print("────┼──────────────────────────────────────────────────┼──────────┼─────────────")
	conn = sqlite3.connect('articles.db')
	c = conn.cursor(); c.execute("SELECT id,title,docreation,articlecategory FROM articles")
	article_list =c.fetchall()
	conn.close()
	list = len(article_list[0])
	arraylen = len(article_list)
	for x in range(0, arraylen):
		index = article_list[x][0]
		title = article_list[x][1]; title = title[:50]
		date = article_list[x][2]
		articlecategory = article_list[x][3]
		if (str(articlecategory) == '0'):
			articlecategory = "   External"
		elif (str(articlecategory) == '1'):
			articlecategory = "   Internal"
		else:
			articlecategory = "***INVALID***"
		print('{index:4}│{title:50}│{date:10}│{articlecategory:13}'\
		.format(index=index, title=title, date=date, \
		articlecategory=articlecategory))
	input("Press Any Key To Continue...")

	return 0

def main():
	print("########################################\n"\
		+ "# Lapam Capital News database updater")
	print("########################################")

	print("########################################")
	print("# New Article......1\n# View Articles:...2\n# Exit:............3")
	print("########################################")
	user_input = ""
	while (user_input != "1" and user_input != "2" and user_input != "3"):
		user_input = input("> ")
	if (user_input == "1"):
		add_article()
	elif (user_input == "2"):
		inspect_articles()
	elif (user_input == "3"):
		return 0	
main() # actually runs program
