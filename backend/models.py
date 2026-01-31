from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime


# defining a schema for the users table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Primary_key= True, index= True)
    full_name = Column(String)
    email = Column(String, unique= True, index= True)
    password_hash = Column(String)
    role = Column(String)

#defining a schema for the doctors table
class Doctors(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    specialization = Column(String)
    hpcsa_number = Column(String, unique=True)
    is_verified = Column(Boolean, default=False )
    consultation_fee = Column(Float) 
    accepted_medical_aids = Column(Text)

class Appointments(Base):
    __tablename_ = "appointments"
    id = Column(Integer, primary_key=True, index= True)
    users_id = Column(Integer, ForeignKey("users.id"))
    doctors_id = Column(Integer, ForeignKey("doctors.id"))
    start_time = Column(DateTime)
    is_emergency = Column(Boolean, default=False)
    status = Column(String, default="pending")









    