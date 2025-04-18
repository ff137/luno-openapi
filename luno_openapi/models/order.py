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


class Order(BaseModel):
    """
    The `base` and `counter` amounts are the principal amounts that were traded, ignoring fees. For example, if the order resulted in a single trade of 1 BTC for 1000 ZAR, then `base`=1 BTC and `counter`=1000 ZAR.  The `fee_base` and `fee_counter` amounts are the fees debited after the trade principal amounts.  For example, for a buy order, `base - base_fee` would be credited to the BTC account and `counter + counter_fee` would be debited from the ZAR account. Similarly, for a sell order, `counter - counter_fee` would be credited to the ZAR account and `base + base_fee` would be debited from the BTC account.
    """  # noqa: E501

    base: Optional[StrictStr] = Field(
        default=None,
        description="Amount of base filled, this value is always positive.",
    )
    completed_timestamp: Optional[StrictInt] = Field(
        default=None,
        description="Time of order completion (Unix milliseconds)  This value is set at the time of this order leaving the order book, either immediately upon posting or later on due to a trade or cancellation. Whilst the order is still pending/live it will be 0.",
    )
    counter: Optional[StrictStr] = Field(
        default=None,
        description="Amount of counter filled, this value is always positive.",
    )
    creation_timestamp: Optional[StrictInt] = Field(
        default=None, description="Time of order creation (Unix milliseconds)"
    )
    expiration_timestamp: Optional[StrictInt] = Field(
        default=None,
        description="Time of order expiration (Unix milliseconds)  This value is set at the time of processing a request from you to cancel the order, otherwise it will be 0.",
    )
    fee_base: Optional[StrictStr] = Field(
        default=None, description="Base amount of fees to be charged"
    )
    fee_counter: Optional[StrictStr] = Field(
        default=None, description="Counter amount of fees to be charged"
    )
    limit_price: Optional[StrictStr] = Field(
        default=None, description="Limit price to transact"
    )
    limit_volume: Optional[StrictStr] = Field(
        default=None, description="Limit volume to transact"
    )
    order_id: Optional[StrictStr] = None
    pair: Optional[StrictStr] = Field(default=None, description="Specifies the market.")
    state: Optional[StrictStr] = Field(
        default=None,
        description="<code>PENDING</code> The order has been placed. Some trades may have taken place but the order is not filled yet.<br> <code>COMPLETE</code> The order is no longer active. It has been settled or has been cancelled.",
    )
    time_in_force: Optional[StrictStr] = Field(
        default=None,
        description="The Time in force option used when the LimitOrder was posted.  Only returned on limit orders.<br> <code>GTC</code> Good 'Til Cancelled. The order remains open until it is filled or cancelled by the user. (default)</br> <code>IOC</code> Immediate Or Cancel. The part of the order that cannot be filled immediately will be cancelled. Cannot be post-only.</br> <code>FOK</code> Fill Or Kill. If the order cannot be filled immediately and completely it will be cancelled before any trade. Cannot be post-only.",
    )
    type: Optional[StrictStr] = Field(
        default=None,
        description="<code>BUY</code> buy market order.<br> <code>SELL</code> sell market order.<br> <code>BID</code> bid (buy) limit order.<br> <code>ASK</code> ask (sell) limit order.",
    )
    __properties: ClassVar[List[str]] = [
        "base",
        "completed_timestamp",
        "counter",
        "creation_timestamp",
        "expiration_timestamp",
        "fee_base",
        "fee_counter",
        "limit_price",
        "limit_volume",
        "order_id",
        "pair",
        "state",
        "time_in_force",
        "type",
    ]

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["PENDING", "COMPLETE"]):
            raise ValueError("must be one of enum values ('PENDING', 'COMPLETE')")
        return value

    @field_validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["BUY", "SELL", "BID", "ASK"]):
            raise ValueError("must be one of enum values ('BUY', 'SELL', 'BID', 'ASK')")
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
        """Create an instance of Order from a JSON string"""
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
        """Create an instance of Order from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "base": obj.get("base"),
                "completed_timestamp": obj.get("completed_timestamp"),
                "counter": obj.get("counter"),
                "creation_timestamp": obj.get("creation_timestamp"),
                "expiration_timestamp": obj.get("expiration_timestamp"),
                "fee_base": obj.get("fee_base"),
                "fee_counter": obj.get("fee_counter"),
                "limit_price": obj.get("limit_price"),
                "limit_volume": obj.get("limit_volume"),
                "order_id": obj.get("order_id"),
                "pair": obj.get("pair"),
                "state": obj.get("state"),
                "time_in_force": obj.get("time_in_force"),
                "type": obj.get("type"),
            }
        )
        return _obj
