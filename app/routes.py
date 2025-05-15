from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.database import SessionLocal
from typing import List
from app.kafka import KafkaProducerSingleton
import json
import logging

router = APIRouter()

@router.get("/order-management/test")
async def test_order_management():
    logging.warning("order-management test hit")
    return {"message": "ok"}
