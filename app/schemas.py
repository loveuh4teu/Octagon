from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ---------- Categories ----------

class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# ---------- Books ----------

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Decimal
    url: Optional[str] = None
    category_id: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    url: Optional[str] = None
    category_id: Optional[int] = None


class BookOut(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)