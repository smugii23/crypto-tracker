from enum import Enum

class Timeframe(Enum):
    HOUR = '1h'
    DAILY = '24h'
    WEEKLY = '7d'
    MONTHLY = '30d'