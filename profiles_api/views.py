from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, response, format = None):
        """Resturns a list of APIView features"""
        an_apiview = ['Uses HTTP methods as function (get, put, post, patch, delete)',
                      'Is similiar to a traditional Django view',
                      'Gives you the most control overe your application logic',
                      'Is mapped mannually to urls'
                      ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
