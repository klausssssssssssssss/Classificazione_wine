from pydantic import BaseModel, Field
from typing import Optional


class Wine(BaseModel):
    alcohol: float = Field(..., example=13.2)
    malic_acid: float = Field(..., example=2.3)
    ash: float = Field(..., example=2.4)
    alcalinity_of_ash: float = Field(..., example=19.5)
    magnesium: float = Field(..., example=98.0)
    total_phenols: float = Field(..., example=2.3)
    flavanoids: float = Field(..., example=2.0)
    nonflavanoid_phenols: float = Field(..., example=0.3)
    proanthocyanins: float = Field(..., example=1.6)
    color_intensity: float = Field(..., example=5.6)
    hue: float = Field(..., example=1.04)
    diluted_wines: float = Field(..., alias="od280/od315_of_diluted_wines", example=3.2)
    proline: float = Field(..., example=1065.0)


    class Config:
        populate_by_name = True  # permette input sia con alias che col nome del campo