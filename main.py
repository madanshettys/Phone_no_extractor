from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

# Define the Pydantic model for the request body
class SIPURIs(BaseModel):
    from_uri: str
    to_uri: str

# Function to extract phone number from SIP URI
def extract_phone_number(sip_uri: str) -> str:
    match = re.search(r'sip:(\+\d+)@', sip_uri)
    return match.group(1) if match else "Not found"

# Define the POST endpoint
@app.post("/extract")
async def extract_numbers(sip_uris: SIPURIs):
    from_number = extract_phone_number(sip_uris.from_uri)
    to_number = extract_phone_number(sip_uris.to_uri)
    return {"from_number": from_number, "to_number": to_number}
