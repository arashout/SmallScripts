def maker(doc_name, string_content, extention="html"):
    """
    Given a doc_name and a string containing html, this function will create a document
    An optional arguement is given if the user wants a different format than html
    """

    doc_start = ""
    doc_end = ""
    if(extention == "html"):
        doc_start = """
        <html>
        <head></head><body>
        """
        doc_end = """
        </body>
        </html>
        """

    with open(doc_name + '.' + extention, 'w') as f:
        f.write(doc_start + string_content + doc_end)

    return 0
