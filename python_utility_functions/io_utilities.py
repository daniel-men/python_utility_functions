import json
from lmdbm import Lmdb

class JsonLmdb(Lmdb):

  def _pre_key(self, value):
    return value.encode("utf-8")

  def _post_key(self, value):
    return value.decode("utf-8")

  def _pre_value(self, value):
    return json.dumps(value).encode("utf-8")
    
  def _post_value(self, value):
    return json.loads(value.decode("utf-8"))