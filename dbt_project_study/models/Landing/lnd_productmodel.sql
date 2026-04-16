SELECT
ProductModelID	
,Name	
,CAST(CatalogDescription AS Nvarchar(max)) as CatalogDescription
,rowguid	
,ModifiedDate
FROM AdventureWorksLT2017.[SalesLT].[ProductModel]