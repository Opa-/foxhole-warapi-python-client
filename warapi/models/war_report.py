# coding: utf-8

"""
    Foxhole WarAPI

    The War API allows developers to query information about the state of the current Foxhole World Conquest.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WarReport(BaseModel):
    """
    WarReport
    """ # noqa: E501
    total_enlistments: Optional[StrictInt] = Field(default=None, alias="totalEnlistments")
    colonial_casualties: Optional[StrictInt] = Field(default=None, alias="colonialCasualties")
    warden_casualties: Optional[StrictInt] = Field(default=None, alias="wardenCasualties")
    day_of_war: Optional[StrictInt] = Field(default=None, alias="dayOfWar")
    __properties: ClassVar[List[str]] = ["totalEnlistments", "colonialCasualties", "wardenCasualties", "dayOfWar"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WarReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WarReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalEnlistments": obj.get("totalEnlistments"),
            "colonialCasualties": obj.get("colonialCasualties"),
            "wardenCasualties": obj.get("wardenCasualties"),
            "dayOfWar": obj.get("dayOfWar")
        })
        return _obj

