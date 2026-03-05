import json
from decimal import Decimal
from typing import Any, Dict, List


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "r", encoding="utf-8") as file:
        trades: List[Dict[str, Any]] = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(str(trade.get("matecoin_price")))

        if bought is not None:
            bought_decimal = Decimal(str(bought))
            matecoin_account += bought_decimal
            earned_money -= bought_decimal * price

        if sold is not None:
            sold_decimal = Decimal(str(sold))
            matecoin_account -= sold_decimal
            earned_money += sold_decimal * price

    result: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file)

