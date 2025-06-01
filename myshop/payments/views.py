from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
import requests
import json
from core.models import Order
from .models import *
import uuid
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from datetime import datetime
from django.contrib import messages


import os
from dotenv import load_dotenv

load_dotenv()  

KHALTI_API_KEY = os.getenv('KHALTI_API_KEY')


# Create your views here.
def initkhalti(request,id):
    data=Order.objects.get(id=id)



   
    url = "https://dev.khalti.com/api/v2/epayment/initiate/"


    
    payload = json.dumps({
        "return_url": "http://127.0.0.1:8000/payments/verifyKhalti/",
        "website_url": "http://127.0.0.1:8000/payments/verifyKhalti/",
        "amount": int(float(data.total))*100,
        
        
        "purchase_order_id": data.id,
        'transaction_id':str(uuid.uuid4()),
        "purchase_order_name": data.product,
        "customer_info": {
        "name": request.user.username,
        "email": request.user.email,
        "phone": request.user.phone,
        }
    })
    headers = {
        'Authorization': f'Key {KHALTI_API_KEY}',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url , headers=headers, data=payload)


    print(response.text)
    

    payment_url=json.loads(response.text)['payment_url']
    return redirect(payment_url)






def verifyKhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/lookup/"
    if request.method == 'GET':
        headers = {
            'Authorization': f'Key {KHALTI_API_KEY}',
            'Content-Type': 'application/json',
        }
        pidx = request.GET.get('pidx')
        transaction_id = request.GET.get('transaction_id')
        purchase_order_id = request.GET.get('purchase_order_id')
        data = json.dumps({
            'pidx':pidx
        })
        res = requests.request('POST',url,headers=headers,data=data)
        new_res = json.loads(res.text)

        try:
            if new_res['status'] == 'Completed':
                order = get_object_or_404(Order, id=purchase_order_id)
                order.is_pay = True
                order.save()

                Transaction.objects.create(
                    order=order,
                    user=request.user,
                    amount=new_res['total_amount'],
                    transaction_id=transaction_id
                )

                subject = 'Payment Successful'
                message = render_to_string('msg.html',{
                    'user': request.user,
                    'product': order.product,
                    'amount':order.total,
                    'date': datetime.now()
                })

                email_msg = EmailMessage(subject, message, to=[request.user.email])

                try:
                    email_msg.send(fail_silently=False)
                    email_sent = True
                    
                except Exception as e:
                    print("Email sending failed:", e)
                    email_sent = False

                return render(request, 'email_verify.html', {
                    'order': order,
                    'email_sent': email_sent
                })

        except Exception as e:
            print("Error during payment verification:", e)
            messages.error(request, "Something went wrong while processing your payment.")
            return redirect('my_order')
        
        messages.error(request, "Payment verification failed.")
        return redirect('my_order')

    else:
        return JsonResponse({'error': 'Invalid request method'},status=400)




