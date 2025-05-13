from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

# Root endpoint to confirm the service is running
@app.get("/", include_in_schema=False)
async def read_root():
    return {"message": "FastAPI phone extractor is running!"}

# Request body schema
class SIPURIs(BaseModel):
    from_uri: str
    to_uri: str

# Phone number extraction logic
def extract_phone_number(sip_uri: str) -> str:
    match = re.search(r'sip:(\+\d+)@', sip_uri)
    return match.group(1) if match else "Not found"

# Main POST endpoint to extract phone numbers
@app.post("/extract")
async def extract_numbers(sip_uris: SIPURIs):
    from_number = extract_phone_number(sip_uris.from_uri)
    to_number = extract_phone_number(sip_uris.to_uri)
    return {
        "from_number": from_number,
        "to_number": to_number
    }
