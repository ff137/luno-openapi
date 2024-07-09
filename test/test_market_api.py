# coding: utf-8

"""
    Luno API

    The Luno API provides developers with a wealth of financial information provided through the Luno platform.  Through this secure system developers can:  <ul>    <li>Create accounts for trading in cryptocurrencies</li>    <li>Access current and historic cryptocurrency market data</li>    <li>Submit trade orders and view order status</li>    <li>Buy and sell Bitcoin and Ethereum</li>    <li>Send and receive Bitcoin and Ethereum</li>    <li>Generate Bitcoin and Ethereum wallet addresses</li>  </ul>   The Luno API brings the world of Bitcoin and Ethereum to your doorstep. 

    The version of the OpenAPI document: 1.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from luno_openapi.api.market_api import MarketApi


class TestMarketApi(unittest.IsolatedAsyncioTestCase):
    """MarketApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = MarketApi()

    def tearDown(self) -> None:
        pass

    def test_get_candles(self) -> None:
        """Test case for get_candles

        Get candles
        """
        pass

    def test_get_order_book(self) -> None:
        """Test case for get_order_book

        Get top order book
        """
        pass

    def test_get_order_book_full(self) -> None:
        """Test case for get_order_book_full

        Get full order book
        """
        pass

    def test_get_ticker(self) -> None:
        """Test case for get_ticker

        Get ticker for currency pair
        """
        pass

    def test_get_tickers(self) -> None:
        """Test case for get_tickers

        List tickers for all currency pairs
        """
        pass

    def test_list_trades(self) -> None:
        """Test case for list_trades

        List recent trades
        """
        pass

    def test_markets(self) -> None:
        """Test case for markets

        Get markets info
        """
        pass


if __name__ == "__main__":
    unittest.main()
