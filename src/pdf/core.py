import pdfkit
import os


def transform(link, filename):
    pdfkit.from_string(link, filename)


if __name__ == "__main__":
    h = """
    <!DOCTYPE html>
    <html>
        <body>
        <center><h1>Test</h1></center>
        </body>
    </html>
    """
    transform(h, 'out.pdf')
