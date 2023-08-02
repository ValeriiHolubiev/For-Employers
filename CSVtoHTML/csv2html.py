def table_start():
	return "<table>\n"

def table_end():
	return "\n\n</table>"

def row_start():
	return "<tr>\n"

def row_end():
	return "</tr>\n"

def coloumn_start():
	return " <td>"

def coloumn_end():
	return "</td>\n"


text = ""

with open("CSVtest.csv") as csv:
	text += table_start()

	for l in csv:
		text += row_start()

		for c in l.split(","):
			text += coloumn_start()

			text += c.rstrip()

			text += coloumn_end()
		
		text += row_end()
		
	text += table_end()

with open ("index.html", "w") as html:
	html.write(text)