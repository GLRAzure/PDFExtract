 # PDFExtract

This project was created to extract text from PDF files and store in CosmosDB.The purpose for this was to show a customer how we can take text from file apply cognitive services to the text to get things like sentiment, key phraes etc and store that information in Cosmos DB. From their we can apply Azure search and LUIS to enable Q&A like capbility to a bot. The repository leverages Cosmos SQL API as well as Table API to persist the data. The ARM template in this repository will deploy the following architecture in Azure and you can deploy the python code to the Azure function.


![alt text](https://raw.githubusercontent.com/RodMeans/GLRAzure/PDFTextExtract/PDFExtract/PDFExtractDiagram.png)

