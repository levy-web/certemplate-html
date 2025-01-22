# from weasyprint import HTML
# import sys

# html = HTML(filename='./certs.html')

# HTML(file_obj=sys.stdin)

# html.write_pdf('/certs.pdf')

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

font_config = FontConfiguration()
html = HTML(filename='./certs.html')
css = CSS(filename='./certs.css')
html.write_pdf(
    './cert.pdf', stylesheets=[css],
    font_config=font_config)

