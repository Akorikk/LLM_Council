# decision_schema.py

from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4


class Dissent(BaseModel):
    agent: str
    reason: str


class DecisionObject(BaseModel):
    decision: str = Field(..., description="APPROVE | REJECT | NEED_MORE_INFO")
    confidence: float = Field(..., ge=0.0, le=1.0)
    summary: str
    risks: List[str]
    citations: List[str]
    dissent: Optional[List[Dissent]] = []
    audit_id: str = Field(default_factory=lambda: str(uuid4()))
