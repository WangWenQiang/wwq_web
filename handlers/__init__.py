import configparser
import pymongo

from urllib.parse import quote_plus
from configparser import ExtendedInterpolation

from tool.common_tool import two_level

cf = configparser.ConfigParser(interpolation=ExtendedInterpolation())
conf_file = two_level(__file__, 'config/conf.ini')
cf.read(conf_file)
host = cf.get('db', 'host')
port = int(cf.get('db', 'port'))
database = cf.get('db', 'database')
user = cf.get('db', 'user')
password = cf.get('db', 'password')

if user:
    conn = pymongo.MongoClient("mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (
        quote_plus(user), quote_plus(password), host, database))
else:
    conn = pymongo.MongoClient(host=host, port=port)
db_link = conn['tomorrow']
