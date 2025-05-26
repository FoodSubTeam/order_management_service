from enum import Enum

class Topic(Enum):
    OFFER_SELECTED = "offer.selected"
    SUBSCRIPTION_PAID = "subscription.paid"
    KITCHEN_ORDER = "kitchen.order"


class MessageType(Enum):
    REQUEST_SUBSCRIPTION_PAYMENT = "request_subscription_payment"
    OFFER_PAYMENT_SUCCESSFUL = "offer_payment_successful"
    OFFER_PAYMENT_FAILURE = "offer_payment_failure"
    MARK_SUBSCRIPTION_AS_PAYED = "mark_subscription_as_paid"
    GENERATE_KITCHEN_ORDERS = "generate_kitchen_orders"