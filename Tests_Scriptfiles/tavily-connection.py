# To install: pip install tavily-python
from tavily import TavilyClient
client = TavilyClient("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")
response = client.search(
    query="best places to visit on  winter" 
)
print(response)