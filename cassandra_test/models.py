import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import create_keyspace_simple


create_keyspace_simple('test', 1)


class CassUserModel(Model):
    user_id    = columns.UUID(primary_key=True, default=uuid.uuid4)
    user_type  = columns.Integer(index=True)
    created_at = columns.DateTime()
    description= columns.Text(required=False)
