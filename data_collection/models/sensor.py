from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    Float,
    UniqueConstraint,
    PrimaryKeyConstraint,
)
from dependencies.db_initializer import Base


class Sensor(Base):
    """Models a sensor table"""

    __tablename__ = "dc_sensor"
    name = Column(String(225), nullable=False, unique=True)
    id = Column(Integer, nullable=False, primary_key=True)
    value = Column(Float, nullable=False)
    alertDirection = Column(Integer, nullable=False)
    upperValueRange = Column(Float, nullable=False, default=0)
    lowerValueRange = Column(Float, nullable=False, default=0)
    # project_id = Column(
    #     Integer,
    #     ForeignKey('project.id', ondelete='CASCADE'),
    #     nullable=False,
    # )

    UniqueConstraint("name", name="uq_sensor_name")
    PrimaryKeyConstraint("id", name="pk_sensor_id")
