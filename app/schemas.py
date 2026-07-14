from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
from datetime import datetime

class OrderItemSchema(BaseModel):
    product_name_raw: str = Field(..., description="Exact name or description of the item ordered as stated or inferred from the text")
    quantity: float = Field(..., description="Numeric quantity of the item")
    unit: Optional[str] = Field("unit", description="Unit of measurement (e.g., kg, box, packet, liters, unit, pcs)")
    unit_price: Optional[float] = Field(None, description="Price per unit if explicitly mentioned in the text")
    line_total: Optional[float] = Field(None, description="Total price for this line item if mentioned or calculated")

class ParsedOrderSchema(BaseModel):
    items: List[OrderItemSchema] = Field(..., description="List of items extracted from the customer's WhatsApp message")
    total_estimate: Optional[float] = Field(None, description="Overall total estimated cost or price if mentioned or computed from items")
    notes: Optional[str] = Field(None, description="Any delivery notes, preferred payment terms, or special instructions mentioned")

class OrderResponseSchema(BaseModel):
    id: str
    business_id: str
    customer_id: str
    source_message_id: Optional[str] = None
    order_time: Optional[datetime] = None
    total_value: Optional[float] = None
    status: str
    raw_parsed: Dict[str, Any]
    created_at: Optional[datetime] = None

class WebhookVerificationResponse(BaseModel):
    status: str
    message: Optional[str] = None
