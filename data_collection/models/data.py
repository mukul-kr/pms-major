from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
    UniqueConstraint,
    PrimaryKeyConstraint,
    ForeignKey,
    DateTime,
)
from datetime import datetime
from sqlalchemy.orm import relationship

from dependencies.db_initializer import Base


class Data(Base):
    """Models a Data table"""

    __tablename__ = "dc_data"
    # __table_args__ = {'extend_existing': True}
    value = Column(Float, nullable=False)
    id = Column(Integer, nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    device_id = Column(
        String(255),
        ForeignKey("dc_device.ext_id", ondelete="SET NULL"),
        nullable=False,
    )
    device = relationship("Device", backref="data")
    sensor_id = Column(
        Integer,
        ForeignKey("dc_sensor.id", ondelete="SET NULL"),
        nullable=False,
    )
    sensor = relationship("Sensor", backref="data")

    UniqueConstraint("name", name="uq_device_name")
    PrimaryKeyConstraint("id", name="pk_device_id")
