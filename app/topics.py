from enum import Enum

class Topic(Enum):
    OFFER_SELECTED = "offer.selected"
    SUBSCRIPTION_PAID = "subscription.paid"
    KITCHEN_ORDER = "kitchen.order"
    PAY_SUBSCRIPTION = "pay_subscription"
    SUBSCRIPTION_CANCELED = "subscription_canceled"
    CANCEL_SUBSCRIPTION = "cancel_subscription"
    DELIVERY_ORDER = "delivery.order"
    SETUP_NEW_CUSTOMER = "setup-new-customer"
    ADD_NEW_CUSTOMER_RESULT = "add_new_customer_result"
    SETUP_NEW_CUSTOMER_RESULT = "setup-new-customer-result"


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
    REQUEST_ADD_NEW_CUSTOMER_METHOD = "request-add-new-customer-method"
    ADD_NEW_CUSTOMER_SUCCESS = "add-new-customer-success"
    ADD_NEW_CUSTOMER_FAILURE = "add-new-customer-failure"
    SETUP_NEW_CUSTOMER_REQUEST = "setup-new-customer-request"
    SETUP_NEW_CUSTOMER_SUCCESS = "setup-new-customer-success"
    SETUP_NEW_CUSTOMER_FAILURE = "setup-new-customer-failure"