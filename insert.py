import couchbase.search as FT
import couchbase.subdocument as SD
#import jwt  # from PyJWT
from couchbase.cluster import Cluster, ClusterOptions, PasswordAuthenticator
from couchbase.exceptions import *
from couchbase.search import SearchOptions
from couchbase.cluster import QueryOptions
from string import ascii_uppercase, digits
from random import choices

CONNSTR = "couchbase://192.168.2.221"
DEFAULT_USER = "sckhoo"
PASSWORD = 'avmcb01'

str_size = 3
id = 1000
entries = 5000
airline = {}

def upsert_document(doc): 
  #print("\nUpsert CAS: ")
  try:
    # key will equal: "airline_8091"
    key = doc["type"] + "_" + str(doc["id"])
    result = cb_coll_default.upsert(key, doc)
    #print(result.cas)
  except Exception as e:
    print(e)


authenticator = PasswordAuthenticator(DEFAULT_USER, PASSWORD)
cluster = Cluster(CONNSTR, ClusterOptions(authenticator))
bucket = cluster.bucket('sckhoo_bucket_01')
cb_coll_default = bucket.default_collection()


for i in range(entries):
    callsign = ''.join(choices(ascii_uppercase, k=3))
    airline['type'] = "airline"
    airline['id'] = id + i
    airline['callsign'] = callsign
    airline['iata'] = ''.join(choices(digits, k=6))
    airline['icao'] = ''.join(choices(digits, k=6))
    airline['name'] = f"{callsign} airline"
    #print(airline)
    upsert_document(airline)

