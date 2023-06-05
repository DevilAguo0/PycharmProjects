import redis

str = redis.StrictRedis()
result = str.set('py1', 'Tom')
print(result)
result=str.set('py1','Jerry')
print(result)
result=str.get('py1')
print(result)
./////////////////////////////////////////////////////.
result=str.delete('py1')
print(result)