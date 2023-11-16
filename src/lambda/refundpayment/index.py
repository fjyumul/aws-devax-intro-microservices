import json

#This function mocks what would be refunding a payment after a sale fails to process (i.e. out of stock)
#For the workshop, we have left this function empty
def lambda_handler(event, context):
    
    return {
        'status': 'success',
        'message': 'Refund completed'
    }
