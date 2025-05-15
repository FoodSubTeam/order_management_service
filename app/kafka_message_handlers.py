from app.kafka import KafkaProducerSingleton
import logging
import json

# Send message to Payment Service - request payment for subscription
async def request_subscription_payment(data):
    # send user_id, customer_id, price_id
    # price_id has to exist before, must be configured together with Product in Stripe Dashboard
    message = {
        "type": "request_subscription_payment",
        "data": {
            "user_id": data.get("user_id"),
            "customer_id": data.get("customer_id"),
            "subscription_id": data.get("subscription_id"),
            "price_id": data.get("price_id")
        }
    }
    KafkaProducerSingleton.produce_message("offer.selected", json.dumps(message))
    logging.warning(f"Sent message: {json.dumps(message)}")


handlers = {
    "request_subscription_payment": request_subscription_payment,
}