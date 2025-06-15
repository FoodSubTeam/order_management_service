from enum import Enum

class Topic(Enum):
    OFFER_SELECTED = "offer.selected"
    SUBSCRIPTION_PAID = "subscription.paid"
    KITCHEN_ORDER = "kitchen.order"
    PAY_SUBSCRIPTION = "pay_subscription"
    SUBSCRIPTION_CANCELED = "subscription_canceled"
    CANCEL_SUBSCRIPTION = "cancel_subscription"
    DELIVERY_ORDER = "delivery.order"


class MessageType(Enum):
    REQUEST_SUBSCRIPTION_PAYMENT = "request_subscription_payment"
    OFFER_PAYMENT_SUCCESSFUL = "offer_payment_successful"
    OFFER_PAYMENT_FAILURE = "offer_payment_failure"
    MARK_SUBSCRIPTION_AS_PAYED = "mark_subscription_as_paid"
    MARK_SUBSCRIPTION_AS_CANCELED = "mark_subscription_as_cancelled"
    SUBSCRIPTION_CANCELED = "subscription_canceled"
    CANCEL_SUBSCRIPTION = "cancel_subscription"
    CANCEL_SUBSCRIPTION_REQUEST = "cancel_subscription_request"
    GENERATE_KITCHEN_ORDERS = "generate_kitchen_orders"
    GENERATE_DELIVERY_ORDERS = "generate_delivery_orders"