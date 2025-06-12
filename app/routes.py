from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.database import SessionLocal
from app.kafka import KafkaProducerSingleton
from app.service import OrderManagementService
from app.topics import Topic, MessageType
from typing import List
import json
import logging

router = APIRouter()
service = OrderManagementService()

# Generate kitchen orders for all subscriptions with status paid
@router.post("/kitchen-orders-paid")
async def generate_kitchen_orders():
    logging.warning("Generate kitchen orders called.")
    subscriptions = await service.get_paid_subscriptions()
    logging.warning(f"subscriptions={subscriptions}")
    offer_ids = [sub["offer_id"] for sub in subscriptions]
    logging.warning(f"has offer ids. ids={offer_ids}")
    offers = await service.fetch_offers(offer_ids)

    extended_offers = []

    for offer in offers:
        sub_info = next((s for s in subscriptions if str(s["offer_id"]) == str(offer["id"])), None)
        if sub_info:
            extended_offer = {
                **offer,
                "user_id": sub_info["user_id"],
                "subscription_id": sub_info["subscription_id"],
                "delivery_address": sub_info["delivery_address"],
            }
            extended_offers.append(extended_offer)

    logging.warning(f"offers extended={extended_offers}")

    message = {
        "type": MessageType.GENERATE_KITCHEN_ORDERS.value,
        "data": extended_offers
    }

    KafkaProducerSingleton.produce_message(Topic.KITCHEN_ORDER.value, json.dumps(message))
    logging.warning("Sent generate kitchen orders message.")

    return {"message": "Sent generate kitchen orders message", "offer_ids": offer_ids}


# Generate delivery orders for the day
#tu tworzymy o 8 rano delivery orders na dany dzień 
@router.post("/delivery-orders-ready")
async def delivery_orders_ready():
    logging.warning("Generate delivery orders called.")
    ready_orders=await service.get_ready_orders()
    logging.warning(f"ready_orders={ready_orders}")

    message = {
       "type": MessageType.GENERATE_DELIVERY_ORDERS.value,
       "data": ready_orders
    }

    KafkaProducerSingleton.produce_message(Topic.DELIVERY_ORDER.value, json.dumps(message))
    logging.warning("Sent generate delivery orders message.")

    return{"message": "Sent generate delivery orders message"}


# Test endpoint
@router.get("/order-management/test")
async def test_order_management():
    logging.warning("order-management test hit")
    return {"message": "ok"}

