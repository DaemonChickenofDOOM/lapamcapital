import os
import sys
import fileinput
import inflect

magic = "#sequencenumber#" 
evenmoremagic = "#name#"

p = inflect.engine()

print ("sequence length:")
iterations = int(input("> ", ))

magellan = open("magellan.html", 'a')
magellan.write('''
	<div class="large-4 medium-4 cell sticky-container" data-sticky-container style="z-index: 665;">
          <div 
            class="sticky callout" 
            data-sticky data-anchor="exampleId" 
            data-sticky-on="large" 
            data-stick-to="DOOM"
            >

            <h4>#title#</h4>

            <ul class="vertical menu" data-magellan>''')

for x in range(0, iterations):
	moremagic = p.number_to_words(x)

	print("name")
	fuckingmagic = input("> " )

	filein  = "template.html"

	fileout	  = "output.html"

	f = open(filein,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(magic, moremagic)
	newerdata = newdata.replace(evenmoremagic, fuckingmagic)

	f = open(fileout,'a')
	f.write(newerdata)
	f.close()

	magellan.write('\n' + '                <li><a href="#' + moremagic + '">' + fuckingmagic + "</a></li>")
magellan.close()