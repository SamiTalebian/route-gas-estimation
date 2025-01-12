from router.serializer import LocationPointsSerializer
from rest_framework.generics import CreateAPIView


class Test(CreateAPIView):
    serializer_class = LocationPointsSerializer

# get the data-points
# ommit the redundent points (draw a rectangle between the points)
# check gas stations after 45 miles from the full gas 
# check if it neds oil
# check every data point with the gas station and see if they are close or not
# calculate the money, IF YES
# repeat till the end

