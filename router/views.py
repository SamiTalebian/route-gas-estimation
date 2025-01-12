from router.serializer import LocationPointsSerializer
from rest_framework.generics import CreateAPIView


class GasRoutePostView(CreateAPIView):
    """
        Finds the path between the given points and calculates the optimum price for gas paying
    """
    serializer_class = LocationPointsSerializer

#### Actions :
# get the data-points
# ommit the redundent gas stations (draw a rectangle between the points)
# check gas stations after X miles from the full gas 
# check if it needs oil
# check every data point with the cheapest gas station and see if they are close or not
# calculate the money, IF YES
# repeat till the end

