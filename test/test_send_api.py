# coding: utf-8

"""
    Luno API

    The Luno API provides developers with a wealth of financial information provided through the Luno platform.  Through this secure system developers can:  <ul>    <li>Create accounts for trading in cryptocurrencies</li>    <li>Access current and historic cryptocurrency market data</li>    <li>Submit trade orders and view order status</li>    <li>Buy and sell Bitcoin and Ethereum</li>    <li>Send and receive Bitcoin and Ethereum</li>    <li>Generate Bitcoin and Ethereum wallet addresses</li>  </ul>   The Luno API brings the world of Bitcoin and Ethereum to your doorstep. 

    The version of the OpenAPI document: 1.2.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from luno_openapi.api.send_api import SendApi


class TestSendApi(unittest.IsolatedAsyncioTestCase):
    """SendApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = SendApi()

    def tearDown(self) -> None:
        pass

    def test_send(self) -> None:
        """Test case for send

        Send
        """
        pass

    def test_send_fee(self) -> None:
        """Test case for send_fee

        Estimate send fees
        """
        pass


if __name__ == "__main__":
    unittest.main()
