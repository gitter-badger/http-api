# -*- coding: utf-8 -*-

""" CUSTOM Models for the relational database """

from rapydo.models.sqlalchemy import db, ExternalAccounts  # , User

# # Add (inject) attributes to User
# setattr(User, 'name', db.Column(db.String(255)))
# setattr(User, 'surname', db.Column(db.String(255)))

# Let iRODS exist and be linked
setattr(ExternalAccounts, 'irodsuser', db.Column(db.String(50)))
# Also save the unity persistent identifier from EUDAT
setattr(ExternalAccounts, 'unity', db.Column(db.String(100)))
