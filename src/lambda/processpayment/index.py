from glob import glob
from random import randint
from datetime import datetime

# keep track of repeat invocations
lastInvokeTime = datetime.min

class PaymentError(Exception):
    pass

# This function takes in an input credit card and processes the payment.
def lambda_handler(event, context):
    #Get the item number from the input 
    item = int(event['itemId'])
    global lastInvokeTime
    
    # Always decline first payment attempt for itemId 42 
    if item == 42:
        print("lastInvokeTime", lastInvokeTime)
        # Is this a retry, i.e. second invocation within 5 seconds?
        if (datetime.now() - lastInvokeTime).total_seconds() < 5:
            lastInvokeTime = datetime.now()
            return event
        else:
            lastInvokeTime = datetime.now()
            raise PaymentError("Payment Processor unreachable")
    # Always fail for itemId 18 or 81 to trigger catcher
    if item == 18 or item == 81:
        raise PaymentError("Payment details invalid")
    
    lastInvokeTime = datetime.now()
    # else then continue and payment is accepted  
    return event
