import datetime
# ----------------------------------------------------------------
# GENERAL CONFIGURATION
# ----------------------------------------------------------------
SECRET_KEY = 'Awsx1Sedc2Drfv**Ftgb4*yhn5Hujm6Awsx1Desf2Asf1$..Sl-@1!!'
# ----------------------------------------------------------------
# JWT CONFIGURATION
# ----------------------------------------------------------------
JWT_SECRET_KEY = 'change_me'
JWT_TOKEN_LOCATION = 'headers'
JWT_REFRESH_TOKEN_VALIDITY_DAYS = datetime.timedelta(days=90)
JWT_ACCESS_TOKEN_VALIDITY_HOURS = datetime.timedelta(hours=2)

# ----------------------------------------------------------------
# MONGO DATABASE CONFIGURATION
# ----------------------------------------------------------------
# MongoDB configuration parameters

MONGODB_DB = 'bitshifter'
MONGODB_HOST = 'ds159344.mlab.com'
MONGODB_PORT = 59344
MONGODB_USERNAME = 'shifter'
MONGODB_PASSWORD = 'Wstinol123.'


# ----------------------------------------------------------------
# NEO4J DATABASE CONFIGURATION
# ----------------------------------------------------------------
NEO4J_USERNAME = 'shifter'
NEO4J_PASSWORD = 'b.ngigs6TLdGbW.nMOTq9xe36TkiDJH'
GRAPHENEDB_URL = 'hobby-kfleidofeielgbkejgnknfpl.dbs.graphenedb.com:24789'

