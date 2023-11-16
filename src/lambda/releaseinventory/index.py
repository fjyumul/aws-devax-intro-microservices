import json

#This function triggers the SNS message to push to customer telling them their order was not able to be filled 
def lambda_handler(event, context):
    
    #Future roadmap idea## --- Add in customizations with the input path for message based on why order couldn't be processed 
    snsmsg = "There was an issue with your purchase request. Please try again later"
        
    return {
        'status': 'completed',
        'message': 'Inventory successfully released'
    }
