from app.kafka import KafkaProducerSingleton
from app.topics import Topic, MessageType
import logging
import json

# Send message to Payment Service - request payment for subscription
async def request_subscription_payment(data):
    # send user_id, customer_id, price_id
    # price_id has to exist before, must be configured together with Product in Stripe Dashboard
    # TODO: query user-service for customer_id
    message = {
        "type": MessageType.REQUEST_SUBSCRIPTION_PAYMENT.value,
        "data": {
            "user_id": data.get("user_id"),
            "customer_id": data.get("customer_id"),
            "offer_id": data.get("offer_id"),
            "subscription_id": data.get("subscription_id"),
            "price_id": data.get("price_id")
        }
    }
    KafkaProducerSingleton.produce_message(Topic.OFFER_SELECTED.value, json.dumps(message))
    logging.warning(f"Sent payment request for offer: {json.dumps(message)}")


async def handle_payment_success(data):
    logging.warning(f"handle_payment_success reached!")
    message = {
        "type": MessageType.MARK_SUBSCRIPTION_AS_PAYED.value,
        "data": {
            "subscription_id": data.get("subscription_id"),
        }
    }
    KafkaProducerSingleton.produce_message(Topic.SUBSCRIPTION_PAID.value, json.dumps(message))
    logging.warning(f"Sent mark subscription as paid request: {json.dumps(message)}")


async def handle_payment_failure(data):
    pass


handlers = {
    MessageType.REQUEST_SUBSCRIPTION_PAYMENT.value: handle_payment_success, # TODO: once we have payment-service request_subscription_payment,
    MessageType.OFFER_PAYMENT_SUCCESSFUL.value: handle_payment_success,
    MessageType.OFFER_PAYMENT_FAILURE.value: handle_payment_failure
}