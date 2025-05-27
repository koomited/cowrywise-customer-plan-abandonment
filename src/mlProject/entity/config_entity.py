from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    host: str
    port: str
    user: str
    password: str
    database_name: str
    sql_query: str
    local_data_file: Path