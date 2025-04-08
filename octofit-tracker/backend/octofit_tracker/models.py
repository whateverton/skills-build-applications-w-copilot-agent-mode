from pymongo import MongoClient

# Remove djongo dependency and refactor models to use pymongo directly
class MongoDBModel:
    def __init__(self, collection_name):
        client = MongoClient('localhost', 27017)
        self.collection = client['octofit_db'][collection_name]

class User(MongoDBModel):
    def __init__(self):
        super().__init__('users')

class Team(MongoDBModel):
    def __init__(self):
        super().__init__('teams')

class Activity(MongoDBModel):
    def __init__(self):
        super().__init__('activity')

class Leaderboard(MongoDBModel):
    def __init__(self):
        super().__init__('leaderboard')

class Workout(MongoDBModel):
    def __init__(self):
        super().__init__('workouts')
