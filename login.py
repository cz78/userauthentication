import cgi
fm = cgi.FieldStorage()
username = fm.getvalue("Username")
password = fm.getvalue("Passwords")
str="Content-type: text/html"
print(str)
print()

import html5function
omarkup = html5function.opening_markup('','','style.css')
cmarkup = html5function.closing_markup()
print(omarkup)
markup += """
<main>

</main>
"""
print(markup)
print(cmarkup)