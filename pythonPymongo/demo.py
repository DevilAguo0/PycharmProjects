import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db_obj = client.school
coll_obj = db_obj.student
coll_obj.insert_one({'学号': 1, '姓名': '小兰', '性别': '女'})
print('集合中共有{}个文档'.format(coll_obj.count_documents({})))
