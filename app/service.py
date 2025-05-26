import httpx
import logging
from fastapi import HTTPException

OFFER_SERVICE_URL = "http://offer-service:80"
SUBSCRIPTION_SERVICE_URL = "http://subscription-service:80"

class OrderManagementService():
    
    async def get_paid_subscriptions(self):
        try:
            async with httpx.AsyncClient() as client:
                subscriptions = await client.get(f"{SUBSCRIPTION_SERVICE_URL}/subscriptions/paid")
                subscriptions.raise_for_status()
                return subscriptions.json()
        except httpx.HTTPStatusError as e:
            logging.warning("HTTPStatusError occured.")
            if e.response.status_code == 404:
                logging.warning("Subscription service not found.")
                raise HTTPException(status_code=404, detail="Subscription service not found")
            raise HTTPException(status_code=502, detail="Subscription service error")
        except httpx.RequestError as e:
            logging.warning("RequestError occured.")
            raise HTTPException(status_code=502, detail=f"Network error: {e}")
        except:
            logging.warning("Some other error occured.")


    
    async def fetch_offers(self, offer_ids):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{OFFER_SERVICE_URL}/offers-by-ids",
                    json={"offer_ids": offer_ids},
                    timeout=10.0
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise HTTPException(status_code=404, detail="Offer not found")
            raise HTTPException(status_code=502, detail="Offer service error")
        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"Network error: {e}")
