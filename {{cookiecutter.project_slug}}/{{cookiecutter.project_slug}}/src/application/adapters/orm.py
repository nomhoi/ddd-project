import logging
from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper

from application.domain import model

logger = logging.getLogger(__name__)

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('username', String(25)),
    Column('email', String(255), nullable=True),
    Column('full_name', String(255), nullable=True),
    Column('disabled', Boolean, nullable=True),
)

def start_mappers():
    logger.info('Starting mappers')
    mapper(model.User, users)
