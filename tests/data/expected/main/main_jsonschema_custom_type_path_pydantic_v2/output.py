# generated by datamodel-codegen:
#   filename:  custom_type_path.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel

from custom import MultipleLineString, SpecialString, TitleString
from custom.collection.array import Friends
from custom.special import UpperString
from custom.special.numbers import Age


class Person(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    firstName: Optional[TitleString] = Field(
        None, description="The person's first name."
    )
    lastName: Optional[UpperString] = Field(None, description="The person's last name.")
    age: Optional[Age] = Field(
        None, description='Age in years which must be equal to or greater than zero.'
    )
    friends: Optional[Friends] = None
    comment: Optional[MultipleLineString] = None


class RootedCustomType(RootModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    root: SpecialString
