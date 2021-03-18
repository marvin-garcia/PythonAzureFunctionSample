import json
import logging
from typing import List
import azure.functions as func

def main(
    events: List[func.EventHubEvent],
    inputblob: func.InputStream,
    outputblob: func.Out[func.InputStream]):

    logging.info("Received batch of %s events" % str(len(events)))
    blob_content = inputblob.read().decode("utf-8")    
    
    output = json.loads(blob_content)
    logging.info("Loaded %s events from blob storage" % str(len(output)))
    
    for event in events:
        output.append(json.loads(event.get_body().decode('utf-8')))

    logging.info("Writing %s events to blob storage" % str(len(output)))
    outputblob.set(json.dumps(output))