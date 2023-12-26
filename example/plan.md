## All fields
```json
{
   "id": "string",
   "dateAdded": "timestamp",
   "dateUpdated": "timestamp",
   "productInfo": {
       "asins": "string",
       "brand": "string",
       "categories": "string",
       "primaryCategories": "string",
       "colors": "string",
       "dimension": "string",
       "ean": "double",
       "imageURLs": "string",
       "keys": "string",
       "manufacturer": "string",
       "manufacturerNumber": "string",
       "name": "string",
       "prices": {
           "maxAmount": "double",
           "minAmount": "double",
           "availability": "string",
           "color": "string",
           "condition": "string",
           "currency": "string",
           "dateAdded": "timestamp",
           "dateSeen": "string",
           "isSale": "boolean",
           "merchant": "string",
           "offer": "string",
           "returnPolicy": "string",
           "shipping": "string",
           "size": "string",
           "sourceURLs": "string"
       },
       "sizes": "string",
       "sourceURLs": "string",
       "upc": "string",
       "weight": "string"
   }
}
```

## Required fields (filter it when returning from redis)
- id
- colors
- dateAdded
- dateUpdated
- brand
- name

- n outputs

```json
"product:78": {
    "id": "string",
    "dateAdded": "timestamp",
    "dateUpdated": "timestamp",
    "productInfo": {
        "brand": "string",
        "colors": "string",
        "categories": "string",
        "name": "string",
        "prices": {
            "maxAmount": "double",
            "minAmount": "double",
            "dateAdded": "timestamp",
        },
    }
}
```
notes:
- key is product:id
- lowercase everything
- multiindex
- **catgories is a string, string,... !!**
- shd I group together based on category and then populate in redis?
   :> no... we have indexes...

- queryOn(brand, color, categories) with n values

```py
# FT index on search parameters
# '$' return the entire root
# have defaults for all query variables!
rs_product.search(Query(f"@color:{color} @dateAdded:{date_added}").return_field("$"))

```

## Df to redis:
```py
dataFrame.write
  .format("redis")\
  .option("host", host)\
  .option("port", port)\
  .option("table", table)\
  .option("password", auth)\
  .mode("Overwrite")\
  .save()
```

