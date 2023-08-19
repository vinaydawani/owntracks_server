"""Stuff to do on initialization of DB"""

import logging

from sqlalchemy.orm import Session


logger = logging.getLogger(__name__)


def init_db(_db: Session) -> None:
    # TODO create superuser
    ...
