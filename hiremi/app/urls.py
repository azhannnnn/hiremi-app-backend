from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
    

# ======================================================================================== #
#                              RESTFUL API ROUTES
# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'discount', DiscountViewSet, basename='discount')
router.register(r'scorecards', ScoreCardViewSet)
router.register(r'corporatediscount', CorporateDiscountViewSet, basename='corporatediscount')
router.register(r'job-applications', JobApplicationViewSet)
router.register(r'internship-applications', InternshipApplicationViewSet)
router.register(r'mentorshipdiscount', MentorshipDiscountViewSet, basename='mentorshipdiscount')
router.register(r'mentorship', MentorshipViewSet, basename='mentorship')
router.register(r'corporatetraining', CorporateViewSet, basename='corporatetraining')
router.register(r'registers', RegisterViewSet, basename='registers')
router.register(r'verification-details', VerificationDetailsViewSet)
# router.register(r'tickets', TicketCreateViewSet, basename='ticket')
router.register(r'fresherjob', FresherJobViewSet, basename='fresherjob')
router.register(r'internship', InternshipViewSet, basename='internship')

# ======================================================================================== #
#                            ADDITIONAL URL PATTERN


urlpatterns = [

    path('login/', LoginAPI.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordOTPView.as_view(), name='forgotpassword'),
    path('otp-validation/', OTPValidationView.as_view(), name='otp-validation'),
    path('password-reset/', PasswordReset.as_view(), name='password-reset'),
    
    path('pay/', InitiatePayment.as_view(), name='initiate_payment'),
    path('callback/', PaytmCallback.as_view(), name='paytm_callback'),
    path('order-status/', OrderStatus.as_view(), name='order-status'),
    path('transactions/', TransactionDetails.as_view(), name='transactions'),

    path('tickets/', TicketCreateAPIView.as_view(), name='ticket-create'),
    # ======================================================================================== #
    
    # Include the router URLs
    path('api/', include(router.urls)),
    


]