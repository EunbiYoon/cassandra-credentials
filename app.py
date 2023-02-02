from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

user_credentials=PlainTextAuthProvider(username='priya',password='priya@123')
cur=Cluster(['10.31.79.1'], port=9042, auth_provider=user_credentials)

session=cur.connect(keyspace='flask')

try:
    session
    print("SUCCESS: CASSANDRA DB CONNECTED")

except:
    print("ERROR: EITHER USERNAME / PASSWORD / KEYSPACE WRONG !!!")

finally:
    cur.shutdown()