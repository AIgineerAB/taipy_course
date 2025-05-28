import pandas as pd
from pathlib import Path
import duckdb
from taipy.gui import Gui
import taipy.gui.builder as tgb 

DATA_DIRECTORY = Path(__file__).parent / "data"

df = pd.read_csv(
    DATA_DIRECTORY / "norway_new_car_sales_by_model.csv", encoding="latin-1"
)


df_year = duckdb.query(
    """
    SELECT 
        year, SUM(quantity) AS Quantity,
    FROM 
        df
    GROUP BY 
        year
    ORDER BY year
"""
).df().iloc[:-1]

print(df_year)

with tgb.Page() as page:
    tgb.text("# Line chart with tgb.chart()", mode = "md")
    tgb.text("## Line chart", mode = "md")

    tgb.chart(
        "{df_year}", x="Year", y = "Quantity"
    )

    tgb.text("## Raw data", mode = "md")
    tgb.table("{df}")
 

if __name__ == "__main__":
    Gui(page = page).run(port = 8080, use_reloader=True, dark_mode=False)