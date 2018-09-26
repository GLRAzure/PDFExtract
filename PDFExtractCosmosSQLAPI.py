
def ExtractText(file):

    import PyPDF2
    import collections
    import os
    import sys
    import pydocumentdb
    import pydocumentdb.document_client as document_client

    config = { 
        'ENDPOINT': 'You Cosmos Endpoint',
        'MASTERKEY': 'Your key',
        'DOCUMENTDB_DATABASE': 'botdata',
        'DOCUMENTDB_COLLECTION': 'bullitins'
    };

    client = document_client.DocumentClient(config['ENDPOINT'], {'masterKey': config['MASTERKEY']})
    db = client.CreateDatabase({ 'id': config['DOCUMENTDB_DATABASE'] })
    collection = client.CreateCollection(db['_self'], { 'id': config['DOCUMENTDB_COLLECTION'] })
    
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    c = collections.Counter(range(number_of_pages))

    for i in c:
        page = read_pdf.getPage(i)
        pagenumber = read_pdf.getPageNumber(page)
        page_content = page.extractText()
        docinfo = read_pdf.getDocumentInfo()
        Title = docinfo.title
        #task = Entity()
        #task.PartitionKey = file
        #task.RowKey = str(pagenumber)
        #task.description =  str(page_content.encode('utf-8'))
        #table_service.insert_entity('Bullitins', task)
        #print(page_content.encode('utf-8'))
        client.CreateDocument(collection['_self'],
        { 
            'Title': Title,
            'Content': page_content 
        })
    #print(document)



#ExtractText('2016 Cadillac Escalade, Chevrolet Suburban and Tahoe and GMC Yukon Service Manual (1).pdf')

ExtractText('test.pdf')


