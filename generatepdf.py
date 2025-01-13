from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

html = HTML(filename='./certs.html')
css = CSS(filename='./certs.css')
html.write_pdf('./cert.pdf', stylesheets=[css])