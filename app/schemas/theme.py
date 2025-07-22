from pydantic import BaseModel, Field
from typing import Optional

class ThemeUpdate(BaseModel):
    primary_color: Optional[str] = Field(None, example="#3498db")
    secondary_color: Optional[str] = Field(None, example="#2ecc71")
    font: Optional[str] = Field(None, example="Roboto")
    dark_mode: Optional[bool] = Field(None, example=True)
