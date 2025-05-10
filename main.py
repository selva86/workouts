import ollama
import yfinance as yf
from pprint import pprint

# Download ollama from https://ollama.com/ and run `ollama run llama3.2:1b` in terminal
# Install yfinance with `pip install yfinance` or `uv add yfinance`

def get_price(ticker):
    """Get latest price for given ticker"""
    stock = yf.Ticker(ticker)
    return stock.history(period='1d')['close'].iloc[-1]

response = ollama.chat(
    'llama3.2',
    messages=[{'role':'user', 'content': 'What is the stock price of Apple?'}],
    tools=[get_price]
)


def main():
    print("Hello from 02-mcp-vs-function-calling!")
    pprint(dict(response))

if __name__ == "__main__":
    main()
