from fastapi import FastAPI, HTTPException, APIRouter, Form
from twilio.rest import Client
from services.twilio_service import TwilioService
from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal


app = FastAPI()
router = APIRouter()


TWILIO_ACCOUNT_SID = "AC79e3bd2101c8ed932ae42a7155713904"
TWILIO_AUTH_TOKEN = "320bd06a21687e12ce769d996c64f636"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/twilio/webhook")
async def twilio_webhook(body: str = Form(...),from_: str = Form(...),to_: str = Form(...), db: Session = Depends(get_db)):
    try:
        from_number = from_.split(":")[-1]
        to_number = to_.split(":")[-1]
        message_body = body.lower()
        print(f"Received message from {from_number}: {message_body}")
        ts = TwilioService(db)
        response = await ts.handle_twilio_message(from_number, message_body)
        send_whatsapp_message(from_number, response)

        return {"message": "Processed successfully"}
    except Exception as e:
        print(f"Error processing message: {e}")
        raise HTTPException(status_code=500, detail="Error processing message")


def send_whatsapp_message(to: str, body: str):
    client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=body,
        to=f"whatsapp:{to}"
    )


app.include_router(router)
