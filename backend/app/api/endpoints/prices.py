from fastapi import APIRouter, HTTPException
import yfinance as yf

router = APIRouter()

@router.get("/")
def get_stock_price(ticker: str, period: str = '1d'):
    """
    Fetches historical stock price data for a given ticker.

    Parameters:
    - ticker (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL'). Ticker you can find on this page: https://finance.yahoo.com/
    - period (str): The period for which to retrieve historical data (default is '1d'). Options include:
        - '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'.

    Returns:
    - dict: Historical stock price data.

    Raises:
    - HTTPException: If no data is found for the given ticker and period (404).
    - HTTPException: If there is an error in fetching the data (400).
    """

    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if data.empty:
            raise HTTPException(status_code=404, detail="No data for the given ticker or period.")
        
        return data.to_dict()
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Data download error: {str(e)}")
