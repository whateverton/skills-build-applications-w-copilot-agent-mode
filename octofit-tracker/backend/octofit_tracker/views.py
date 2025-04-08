from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'http://localhost:8000/api/users/',
        'teams': 'http://localhost:8000/api/teams/',
        'activities': 'http://localhost:8000/api/activities/',
        'leaderboard': 'http://localhost:8000/api/leaderboard/',
        'workouts': 'http://localhost:8000/api/workouts/',
    })
