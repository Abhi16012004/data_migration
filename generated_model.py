from sqlalchemy import UUID, create_engine, Column, String, Boolean, JSON, ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
 
Base = declarative_base()
 
def generate_uuid():
    return str(uuid.uuid4())
 
class MyModel(Base):
    __tablename__ = 'business_processes'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fqnhash = Column(String)
    json = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
 
    application = relationship("Applications", back_populates="businessprocess")
    division = relationship("Division", uselist=False, back_populates="businessprocess")
    controls = relationship("Controls", back_populates="businessprocess")
 
class Applications(Base):
    __tablename__ = 'applications'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fonihash = Column(String)
    son = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
    businessprocess_id = Column(ForeignKey('business_processes.id'))
 
    businessprocess = relationship("BusinessProcesses", back_populates="application")
    dataplatforms = relationship("DataPlatforms", back_populates="application")
 
class Division(Base):
    __tablename__ = 'division'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fqnhash = Column(String)
    json = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
    businessprocess_id = Column(ForeignKey('business_processes.id'))
 
    businessprocess = relationship("BusinessProcesses", back_populates="division")
 
class DataPlatforms(Base):
    __tablename__ = 'data_platforms'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    application_id = Column(ForeignKey('applications.id'))
 
    application = relationship("Applications", back_populates="dataplatforms")
    databases = relationship("Database", back_populates="dataplatform")
 
class Database(Base):
    __tablename__ = 'database'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fqnhash = Column(String)
    json = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
    dataplatform_id = Column(ForeignKey('data_platforms.id'))
 
    dataplatform = relationship("DataPlatforms", back_populates="databases")
    database_tables = relationship("DatabaseTables", back_populates="database")
 
class DatabaseTables(Base):
    __tablename__ = 'database_tables'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fqnhash = Column(String)
    json = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
    database_id = Column(ForeignKey('database.id'))
 
    database = relationship("Database", back_populates="database_tables")
    attributes = relationship("Attributes", back_populates="database_table")
 
class Attributes(Base):
    __tablename__ = 'attributes'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fqnhash = Column(String)
    json = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
    database_table_id = Column(ForeignKey('database_tables.id'))
 
    database_table = relationship("DatabaseTables", back_populates="attributes")
 
class Controls(Base):
    __tablename__ = 'controls'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fqnhash = Column(String)
    json = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
    businessprocess_id = Column(ForeignKey('business_processes.id'))
 
    businessprocess = relationship("BusinessProcesses", back_populates="controls")
    risk_registers = relationship("RiskRegister", back_populates="control")
 
class RiskRegister(Base):
    __tablename__ = 'risk_register'
 
    id = Column(UUID(as_uuid=True),primary_key=True,default=generate_uuid)
    name = Column(String)
    fqnhash = Column(String)
    json = Column(JSON)
    updatedby = Column(String)
    updatedat = Column(Integer)
    deleted = Column(Boolean)
    control_id = Column(ForeignKey('controls.id'))
 
    control = relationship("Controls", back_populates="risk_registers")