from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import null

from ..FRONEND_ORM_SQL.database import Base


class Svetki(Base):
    __tablename__ = "svetki"
    id = Column(Integer, primary_key=True, nullable= False )
    vārds_uzvards = Column(String, nullable=False, unique=True)
    dzimšanasd = Column(Integer, nullable=False)
    vārdad = Column(Integer, nullable=False)
     