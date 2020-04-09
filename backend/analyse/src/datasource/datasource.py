from pymongo import MongoClient


class MongoDataSource():
    def __init__(self):
        pass

    def _get_client(self):
        username = 'fetcher'
        password = 'iamnotfetcher'
        client = MongoClient('mongodb://%s:%s@47.106.132.194/hotwords_spider' %
                             (username, password))
        return client

    def _get_database(self, database):
        database = self._get_client()[database]
        return database

    def _get_collection(self, database, collection):
        collection = self._get_database(database)[collection]
        return collection

    def _get_datasource(self):
        collection = self._get_collection('hotwords_spider', 'data')
        return collection

    def get_recent_data(self, limit=-1):
        collection = self._get_datasource()
        # print(collection.find({'from': 'weibo'}).count())
        data = []
        if limit == -1:
            res = collection.find({'from': 'weibo'}, {'_id': 0})
        else:
            res = collection.find({
                'from': 'weibo'
            }, {
                '_id': 0,
                'data.url': 0,
                'data.num': 0
            }).skip(collection.find({
                'from': 'weibo'
            }).count() - limit)
        for i in res:
            data.append(i)
        return data

    def get_latest_data(self):
        collection = self._get_datasource()
        res = collection.find({}, {
            '_id': 0,
            'from': 1,
            'updateTime': 1,
            'data.key': 1,
            'data.num': 1
        })
        if res.count() > 0:
            return res[0]
        else:
            return None
