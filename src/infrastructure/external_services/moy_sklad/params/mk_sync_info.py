from dataclasses import dataclass
import datetime


@dataclass
class MKSyncInfoCreateParams:
    synced_at: datetime.datetime = None
    prod_synced_at: datetime.datetime = None
    cat_synced_at: datetime.datetime = None
