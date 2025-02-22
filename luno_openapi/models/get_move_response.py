# coding: utf-8

"""
Luno API

The Luno API provides developers with a wealth of financial information provided through the Luno platform.  Through this secure system developers can:  <ul>    <li>Create accounts for trading in cryptocurrencies</li>    <li>Access current and historic cryptocurrency market data</li>    <li>Submit trade orders and view order status</li>    <li>Buy and sell Bitcoin and Ethereum</li>    <li>Send and receive Bitcoin and Ethereum</li>    <li>Generate Bitcoin and Ethereum wallet addresses</li>  </ul>   The Luno API brings the world of Bitcoin and Ethereum to your doorstep.

The version of the OpenAPI document: 1.2.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Self


class GetMoveResponse(BaseModel):
    """
    GetMoveResponse response for GET /1/move
    """  # noqa: E501

    amount: Optional[StrictStr] = Field(
        default=None,
        description="The assets quantity to move from the debit account to credit account. This is always a positive value.",
    )
    client_move_id: Optional[StrictStr] = Field(
        default=None, description="User defined unique ID"
    )
    created_at: Optional[StrictInt] = Field(
        default=None, description="Unix time the move was initiated, in milliseconds"
    )
    credit_account_id: Optional[StrictStr] = Field(
        default=None, description="The account to credit the funds to."
    )
    debit_account_id: Optional[StrictStr] = Field(
        default=None, description="The account to debit the funds from."
    )
    id: Optional[StrictStr] = Field(
        default=None, description="Unique ID, defined by Luno"
    )
    status: Optional[StrictStr] = Field(
        default=None,
        description="Current status of the move.  Status meaning:<br> <code>CREATED</code> The move is awaiting execution.<br> <code>MOVING</code> The funds have been reserved and the move is being executed.<br> <code>SUCCESSFUL</code> The move has completed successfully and should be reflected in both accounts available balance.<br> <code>FAILED</code> The move has failed. There could be many reasons for this but the most likely is that the debit account doesn't have enough available funds to move.<br>",
    )
    updated_at: Optional[StrictInt] = Field(
        default=None, description="Unix time the move was last updated, in milliseconds"
    )
    __properties: ClassVar[List[str]] = [
        "amount",
        "client_move_id",
        "created_at",
        "credit_account_id",
        "debit_account_id",
        "id",
        "status",
        "updated_at",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["CREATED", "MOVING", "SUCCESSFUL", "FAILED"]):
            raise ValueError(
                "must be one of enum values ('CREATED', 'MOVING', 'SUCCESSFUL', 'FAILED')"
            )
        return value

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
        """Create an instance of GetMoveResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetMoveResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "amount": obj.get("amount"),
                "client_move_id": obj.get("client_move_id"),
                "created_at": obj.get("created_at"),
                "credit_account_id": obj.get("credit_account_id"),
                "debit_account_id": obj.get("debit_account_id"),
                "id": obj.get("id"),
                "status": obj.get("status"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
