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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from warapi.models.faction_enum import FactionEnum
from typing import Optional, Set
from typing_extensions import Self

class War(BaseModel):
    """
    War
    """ # noqa: E501
    war_id: Optional[StrictStr] = Field(default=None, alias="warId")
    war_number: Optional[StrictInt] = Field(default=None, alias="warNumber")
    winner: Optional[FactionEnum] = None
    conquest_start_time: Optional[StrictInt] = Field(default=None, alias="conquestStartTime")
    conquest_end_time: Optional[StrictInt] = Field(default=None, alias="conquestEndTime")
    resistance_start_time: Optional[StrictInt] = Field(default=None, alias="resistanceStartTime")
    required_victory_towns: Optional[StrictInt] = Field(default=None, alias="requiredVictoryTowns")
    __properties: ClassVar[List[str]] = ["warId", "warNumber", "winner", "conquestStartTime", "conquestEndTime", "resistanceStartTime", "requiredVictoryTowns"]

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
        """Create an instance of War from a JSON string"""
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
        """Create an instance of War from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "warId": obj.get("warId"),
            "warNumber": obj.get("warNumber"),
            "winner": obj.get("winner"),
            "conquestStartTime": obj.get("conquestStartTime"),
            "conquestEndTime": obj.get("conquestEndTime"),
            "resistanceStartTime": obj.get("resistanceStartTime"),
            "requiredVictoryTowns": obj.get("requiredVictoryTowns")
        })
        return _obj

