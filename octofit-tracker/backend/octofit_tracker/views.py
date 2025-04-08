from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://congenial-giggle-g46rqpj9gxp2vvg4-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/',
    })
