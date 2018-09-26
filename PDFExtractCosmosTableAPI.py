
def ExtractText(file):

    import PyPDF2
    import collections
    import os
    import sys
    from azure.cosmosdb.table.tableservice import TableService
    from azure.cosmosdb.table.models import Entity
    
    table_service = TableService(connection_string='<your connection string')


    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    c = collections.Counter(range(number_of_pages))

    for i in c:
        page = read_pdf.getPage(i)
        pagenumber = read_pdf.getPageNumber(page)
        page_content = page.extractText()
        docinfo = read_pdf.getDocumentInfo()
        docinfo = docinfo.title
        #task = Entity()
        #task.PartitionKey = file
        #task.RowKey = str(pagenumber)
        #task.description =  str(page_content.encode('utf-8'))
        #table_service.insert_entity('Bullitins', task)
        #print(page_content.encode('utf-8'))
        print(docinfo)



#ExtractText('2016 Cadillac Escalade, Chevrolet Suburban and Tahoe and GMC Yukon Service Manual (1).pdf')

ExtractText('test.pdf')


