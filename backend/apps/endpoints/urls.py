from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView
from apps.endpoints.views import ABTestViewSet
from apps.endpoints.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")


urlpatterns = [
    path(r"api/v1/", include(router.urls)),
    # add predict url
    path('api/v1/income_classifier/predict', PredictView.as_view(), name='predict'),
    path('api/v1/stop_ab_test/<int:ab_test_id>/', StopABTestView.as_view(), name='stop_ab_test'),]