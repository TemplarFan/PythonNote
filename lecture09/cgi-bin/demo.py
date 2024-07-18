import cgi

form = cgi.FieldStorage()

print('Content-type:text/html \n\n')

print("<h1>HELLO NEU.</h1>")

print("<h1>hello, {}</h1>".format( form["name"].value))