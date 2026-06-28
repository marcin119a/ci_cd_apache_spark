from pyspark.sql import DataFrame
from pyspark.sql import functions as F

from src.us_accidents_etl.config.settings import ETLConfig


def filter_high_severity(df: DataFrame, cfg: ETLConfig) -> DataFrame:
    return df.filter(F.col("Severity") >= cfg.min_severity)

"""
@TODO: Add more filters here as needed, e.g., filter by state, date range, etc.
"""
def filter_weather_conditions(df: DataFrame, cfg: ETLConfig) -> DataFrame:
    """Filtruje wypadki na podstawie dozwolonych warunków pogodowych z konfiguracji."""
    return df.filter(F.col("Weather_Condition").isin(cfg.weather_conditions))


def apply_etl_filters(df: DataFrame, cfg: ETLConfig) -> DataFrame:
    # Przepuszczamy DataFrame przez pierwszy filtr...
    df = filter_high_severity(df, cfg)

    # ...a następnie przez filtr pogodowy
    df = filter_weather_conditions(df, cfg)

    return df