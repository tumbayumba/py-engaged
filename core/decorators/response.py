import json
from functools import wraps

def sender(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Call the original function and get the return value (message)
        message = func(self, *args, **kwargs)
        
        # Format the message as a JSON response and send it
        return self.send(message)  # Call self.send to output the JSON content
    
    return wrapper