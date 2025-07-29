import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/trade-expanding-llc-trade-expanding-llc-default/api/bin-ip-checker'

mcp = FastMCP('bin-ip-checker')

@mcp.tool()
def iplookup(ip: Annotated[str, Field(description='')]) -> dict: 
    '''IP Address Lookup'''
    url = 'https://bin-ip-checker.p.rapidapi.com/ip-lookup'
    headers = {'x-rapidapi-host': 'bin-ip-checker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ip': ip,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bin_ipchecker(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Shield your business from fraud effortlessly with our powerful, free BIN lookup API. Prevent fraudulent credit card transactions with ease by verifying, validating, and scrutinizing card details using BIN numbers. Our extensive database, boasting millions of BINs, ensures unparalleled accuracy, giving you peace of mind in every transaction. Harness the power of our BIN lookup solution to safeguard your revenue and maintain security for your business. --(Just Updated) Designed with online merchants in mind, our API offers comprehensive insights into credit/debit card transactions, empowering businesses to assess transaction risk effectively. However, its flexibility allows anyone to utilize it across various platforms, tailored to their specific needs and plan limits.'''
    url = 'https://bin-ip-checker.p.rapidapi.com/'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'bin-ip-checker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def binchecker(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Shield your business from fraud effortlessly with our powerful, free BIN lookup API. Prevent fraudulent credit card transactions with ease by verifying, validating, and scrutinizing card details using BIN numbers. Our extensive database, boasting millions of BINs, ensures unparalleled accuracy, giving you peace of mind in every transaction. Harness the power of our BIN lookup solution to safeguard your revenue and maintain security for your business. --(Just Updated) Designed with online merchants in mind, our API offers comprehensive insights into credit/debit card transactions, empowering businesses to assess transaction risk effectively. However, its flexibility allows anyone to utilize it across various platforms, tailored to their specific needs and plan limits.'''
    url = 'https://bin-ip-checker.p.rapidapi.com/'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'bin-ip-checker.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
