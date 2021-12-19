from pydantic import BaseModel

class Partition(BaseModel):
  db: str
  table: str