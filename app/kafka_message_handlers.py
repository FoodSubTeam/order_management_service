from app.kafka import KafkaProducerSingleton
from app.topics import Topic, MessageType
import logging
import json

# Send message to Payment Service - request payment for subscription
async def request_subscription_payment(data):
    # TODO: query user-service for customer_id
    customer_id = "cus_S2ZmCvDwZYXCCE"
    message = {
        "type": MessageType.REQUEST_SUBSCRIPTION_PAYMENT.value,
        "data": {
            "user_id": data.get("user_id"),
            "customer_id": customer_id,
            "offer_id": data.get("offer_id"),
            "subscription_id": data.get("subscription_id"),
            "price_id": data.get("price_id")
        }
    }
    KafkaProducerSingleton.produce_message(Topic.PAY_SUBSCRIPTION.value, json.dumps(message))
    logging.warning(f"Sent payment request for offer: {json.dumps(message)}")


async def handle_payment_success(data):
    logging.warning(f"handle_payment_success reached!")
    message = {
        "type": MessageType.MARK_SUBSCRIPTION_AS_PAYED.value,
        "data": data
    }
    KafkaProducerSingleton.produce_message(Topic.SUBSCRIPTION_PAID.value, json.dumps(message))
    logging.warning(f"Sent mark subscription as paid request: {json.dumps(message)}")


async def handle_payment_failure(data):
    pass


async def request_cancel_subscription(data):
    message = {
        "type": MessageType.CANCEL_SUBSCRIPTION.value,
        "data": data
    }
    KafkaProducerSingleton.produce_message(Topic.CANCEL_SUBSCRIPTION.value, json.dumps(message))
    logging.warning(f"Cancel subscription request sent: {json.dumps(message)}")


async def handle_subscription_cancelled(data):
    message = {
        "type": MessageType.MARK_SUBSCRIPTION_AS_CANCELED.value,
        "data": {
            "subscription_id": data.get("subscription_id"),
        }
    }
    KafkaProducerSingleton.produce_message(Topic.SUBSCRIPTION_CANCELED.value, json.dumps(message))
    logging.warning(f"Sent mark subscription as canceled request: {json.dumps(message)}")


handlers = {
    MessageType.REQUEST_SUBSCRIPTION_PAYMENT.value: request_subscription_payment,
    MessageType.OFFER_PAYMENT_SUCCESSFUL.value: handle_payment_success,
    MessageType.OFFER_PAYMENT_FAILURE.value: handle_payment_failure,
    MessageType.SUBSCRIPTION_CANCELED.value: handle_subscription_cancelled,
    MessageType.CANCEL_SUBSCRIPTION_REQUEST.value: request_cancel_subscription
}