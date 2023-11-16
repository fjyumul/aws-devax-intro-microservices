import json
import random

class InventoryError(Exception):
    pass

##Takes an input of a number and checks to see if it is within a list. Items 17 and 71 will be out of stock 
def lambda_handler(event, context):
    
    #Get the item number from the input 
    item = int(event['itemId'])
    print(item)
    
    #Get the payment type from the input 
    paymentType = (event['paymentType'])
    print(paymentType)
    
    #Checking if itemID is valid 
    if 0 > item or item > 100: 
        raise ValueError("Please enter a valid inventory ID 1-100!")
        
    #Check if the itemID is in stock
    itemsNotInStock = [17,71]
    if item in itemsNotInStock: 
        stockErr = "Item " + str(item) + " is not in stock"
        print(stockErr)
        raise InventoryError(stockErr)
        
    return {
        'itemId': str(item),
        'paymentType': paymentType,
        'item': {
            'inStock': True,
            'quantity': random.randint(1, 100),
            'listPrice': round(random.uniform(4.99,200), 2)
        }
    }
