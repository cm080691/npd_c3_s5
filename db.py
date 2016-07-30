from pymongo import MongoClient

client = MongoClient()
test_obj = {'a': 'abc', 'b': 'xyz', 'c': 'asd'}
my_collection = client.my_database.my_collection


def find_object(primary_key):
    '''Finds and returns an object matching the primary key.
    Returns None if not found'
    '''
    my_object = my_collection.find_one({'b':primary_key }, {'_id': 0})
    return my_object

def update_object(new_object):
    '''Updates an object if it exxists, inserts if does not exists'''
   # test_obj = my_collection.find_one({'a': 'abc'})
    my_collection.update({'b': new_object['b']}, new_object, upsert=True)

def remove_object(primary_key):
    '''deletes the object mstching primary_key.
    returns True if deleted, False if not found'''
    del_result = my_collection.delete_one({'b':primary_key})
    return del_result.deleted_count > 0
