from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.middleware.csrf import get_token
import uuid


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Payment System'
        # Force CSRF token creation
        get_token(self.request)
        return context


@method_decorator(csrf_exempt, name='dispatch')
class CreatePaymentSessionView(View):
    def post(self, request, *args, **kwargs):
        return self._process_payment(request)
    
    def get(self, request, *args, **kwargs):
        return self._process_payment(request)
    
    def _process_payment(self, request):
        sslcz = SSLCOMMERZ(settings.SSLCOMMERZ_SETTINGS)
        
        # Generate unique transaction ID
        transaction_id = str(uuid.uuid4().hex)[:10]
        
        # Build absolute URLs with request
        success_url = request.build_absolute_uri('/payment/success/')
        fail_url = request.build_absolute_uri('/payment/fail/')
        cancel_url = request.build_absolute_uri('/payment/cancel/')
        
        post_body = {
            'total_amount': 700,
            'currency': "BDT",
            'tran_id': transaction_id,
            'success_url': success_url,
            'fail_url': fail_url,
            'cancel_url': cancel_url,
            'emi_option': 0,
            'cus_name': "Test Customer",
            'cus_email': "test@example.com",
            'cus_phone': "01700000000",
            'cus_add1': "Customer Address",
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 1,
            'product_name': "Test Product",
            'product_category': "Test Category",
            'product_profile': "general"
        }

        try:
            response = sslcz.createSession(post_body)
            if 'GatewayPageURL' in response:
                return redirect(response['GatewayPageURL'])
            else:
                return HttpResponse("Payment initialization failed! Please try again.")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")


@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccessView(TemplateView):
    template_name = 'payment/success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get data from either GET or POST depending on how the gateway redirected
        data = self.request.GET.dict() if self.request.GET else self.request.POST.dict()
        
        # Process and clean up the payment data
        payment_info = {
            'transaction_id': data.get('tran_id', ''),
            'amount': data.get('amount', ''),
            'currency': data.get('currency', 'BDT'),
            'card_type': data.get('card_type', ''),
            'payment_status': data.get('status', 'VALID'),
            'bank_transaction_id': data.get('bank_tran_id', ''),
            'validation_id': data.get('val_id', ''),
            'transaction_date': data.get('tran_date', ''),
            'card_issuer': data.get('card_issuer', ''),
            'card_brand': data.get('card_brand', ''),
            'card_issuer_country': data.get('card_issuer_country', ''),
            'store_amount': data.get('store_amount', ''),
        }
        
        # Add both raw data and processed data to context
        context['payment_data'] = data
        context['payment_info'] = payment_info
        return context
        
    def post(self, request, *args, **kwargs):
        # Handle POST requests from payment gateway
        return self.render_to_response(self.get_context_data(**kwargs))


@method_decorator(csrf_exempt, name='dispatch')
class PaymentFailView(TemplateView):
    template_name = 'payment/fail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_data'] = self.request.GET
        return context
        
    def post(self, request, *args, **kwargs):
        # Handle POST requests from payment gateway
        context = self.get_context_data(**kwargs)
        context['payment_data'] = request.POST
        return self.render_to_response(context)


@method_decorator(csrf_exempt, name='dispatch')
class PaymentCancelView(TemplateView):
    template_name = 'payment/cancel.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_data'] = self.request.GET
        return context
        
    def post(self, request, *args, **kwargs):
        # Handle POST requests from payment gateway
        context = self.get_context_data(**kwargs)
        context['payment_data'] = request.POST
        return self.render_to_response(context)


@method_decorator(csrf_exempt, name='dispatch')
class IPNHandlerView(View):
    def post(self, request, *args, **kwargs):
        sslcz = SSLCOMMERZ(settings.SSLCOMMERZ_SETTINGS)
        post_body = request.POST.dict()
        
        try:
            if sslcz.hash_validate_ipn(post_body):
                response = sslcz.validationTransactionOrder(post_body['val_id'])
                print("Transaction Validated:", response)
                return HttpResponse("IPN Validation Successful")
            else:
                print("Hash validation failed")
                return HttpResponse("IPN Validation Failed")
        except Exception as e:
            print(f"IPN Error: {str(e)}")
            return HttpResponse(f"IPN Error: {str(e)}")
            
    def get(self, request, *args, **kwargs):
        return HttpResponse("Invalid Request")