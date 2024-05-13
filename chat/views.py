from django.shortcuts import render as re
from django.shortcuts import redirect as rd
from django.http import HttpResponse, JsonResponse
from chat.models import Users,Message
from datetime import datetime
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import razorpay
# Create your views here.
ottt=0
new_password=0
fpg=-1
new_usersss=0
def otp():
    return int(r.uniform(1000,4444))
def send_email(email,ot):
            try:
                msg = MIMEMultipart()
                print("[+] Message Object Created")
            except:
                print("[-] Error in Creating Message Object")
                return
            fromaddr='monsterrazzy@gmail.com'
            toaddr=email

            msg['From'] = fromaddr

            msg['To'] = toaddr

            msg['Subject'] = 'Reset Password'
            # ot=color.BOLD + str(ot) + color.END
            print(ot)
            body = 'Your OTP is:'+str(ot)

            msg.attach(MIMEText(body, 'plain'))

          

          

            

            try:
                s = smtplib.SMTP('smtp.gmail.com', 587) 
                # s = smtplib.SMTP('stud.iitp.ac.in', 587)
                print("[+] SMTP Session Created")
            except:
                print("[-] Error in creating SMTP session")
                return

            s.starttls()

            try:
                s.login(fromaddr, 'qekborrfsfieqpsh')
                print("[+] Login Successful")
            except:
            
                print("[-] Login Failed")

            text = msg.as_string()

            try:
                s.sendmail(fromaddr, toaddr, text)
                print("[+] Mail Sent successfully")
            except:
                print('[-] Mail not sent')

            s.quit()

def home(request):
    return re(request,'home.html')



def room(request,room):
    username = request.GET.get('username')
    
   
    a=Users.objects.filter(name=room).values();
    
    a=a[0]['image']
    
    # return re(request,'room.html')
    return re(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room,
        'image':a

      
        
    })
    
    




def checkrecipent(request):
    # room=request.POST['rn']
    room=request.POST['room_id']
    ff=request.POST['username']
    # if(Message.objects.filter(user=ff,recipent=room).exists()):
    #     return rd('/'+room+'/?userame='+ff)
    # else:
    #     ss=Message.objects.create(user=)
    #     ss.save()
    print(room)
    print(ff)
    return rd('/'+room+'/?username='+ff)

    # if(Users.objects.filter(name=recipent_name).exists()):



def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    # print(message)
    # print(username,'->',room_id)

    
    new_message = Message.objects.create(value=message, user=username,recipent=room_id,xx=str(datetime.now()))
    new_message.save()
    return HttpResponse('Message sent successfully')   

def getMessages(request, room,username):
    room_details = Users.objects.get(name=room)
    # print(username+'->'+room)
    messages1= Message.objects.filter(user=room,recipent=username)
    messages2=Message.objects.filter(user=username,recipent=room)
    a1=[]
 
    for i in (list(messages1.values())):
        a1.append([i['xx'],i,0])
    for i in (list(messages2.values())):
        a1.append([i['xx'],i,1])
    a1.sort()
    # print(a1)
    ans=[]
    for i in a1:
        ans.append(i[1])
    value=[]
    for i in a1:
        value.append(i[2])
    a=Users.objects.filter(name=room);
    b=Users.objects.filter(name=username);
    a=list(a.values())
    b=list(b.values())
    
    meimg=a[0]['image']
    reimg=b[0]['image']
    nickname=b[0]['nickname']
    

 


    return JsonResponse({"messages":ans,'value':value,'nickname':nickname,'meimg':meimg,'reimg':reimg})
 
def data(request):
    nic=request.POST['ni']
   
    
    
    u=request.POST['Choose']
    usrname,img=u.split(' ')
    b=Users.objects.all().values();

    b=b[1:]
    print(nic)
    print(u)
  
    

   
   
    if(Users.objects.filter(nickname=nic).exists()):
        qq=False
        return re(request,'data.html',{'error':'error','usern':usrname})
    else:
    
        a= Users.objects.get(name=usrname)
    
        a.nickname=nic
        a.image=img
        a.save()
    


    
        return re(request,'home.html')


def check(request):
    user_name=request.GET.get('em',0)
    user_password=request.GET.get('ps',0)
    user_signup=request.GET.get('sb',0)
    user_login=request.GET.get('lb',0)
    user_forgot=request.GET.get('fg',0)
    global ottt
    # print(user_signup)
    # print(user_login)
    global fpg
    if(user_signup):
        if(user_name=="" or user_password==""):
            return re(request,'home.html',{'error11':'error11'})
        elif(Users.objects.filter(name=user_name).exists()):
            return re(request,'home.html',{'error1':'error1'})
        
        else:
            new_username=Users.objects.create(name=user_name,password=user_password)
            new_username.save()
            ot=otp()
            ottt=ot
            fpg=user_name
            send_email(user_name,ot)
            return re(request,'otp1.html',{'email':user_name})
        
    elif(user_login):
        if(user_name=="" or user_password==""):
            return re(request,'home.html',{'error11':'error1'})
        elif(Users.objects.filter(name=user_name).exists()):
            if(Users.objects.filter(name=user_name,password=user_password).exists()):
                b=Users.objects.all().values()
                b=b[1:]
            
                f={'my_values':b,'usern':user_name}
                return re(request,'extra.html',f)
            else:
                return re(request,'home.html',{'error2':'error2'})

        else:
    
            
            return re(request,'home.html',{'error3':1})
    elif(user_forgot):
        

        return re(request,'forgot.html') 
    else:
        return re(request,'payment.html')  
def forgot(request):
    global ottt
    global new_password
    global new_usersss
    username=request.POST['nm']
    email=request.POST['nm']
    password=request.POST['pss']
    
    submit=request.POST['sl']

    if(submit):
        if(Users.objects.filter(name=username).exists()):
            new_usersss=username
            new_password=password
            ot=otp()
            ottt=ot
            send_email(email,ot)
            return re(request,'otp.html',{'email':email})
        else:
            return re(request,'forgot.html',{'error':'error'})
       
def otpp(request):
    
    f=request.POST['first']
    s=request.POST['second']
    t=request.POST['third']
    fo=request.POST['fourth']
    sp=request.POST['sp']
    
    if(sp):
        x=f+s+t+fo
 
        if(str(ottt)==x):
            a= Users.objects.get(name=new_usersss)
    
            a.password=new_password
        

            a.save()
            
            return re(request,'otp.html',{'error1':'error'})
        else:
            return re(request,'otp.html',{'error':1})
    
def otp1(request):
    
    f=request.POST['first']
    s=request.POST['second']
    t=request.POST['third']
    fo=request.POST['fourth']
    sp=request.POST['sp']
    
    if(sp):
        x=f+s+t+fo
 
        if(str(ottt)==x):
        
            
            return re(request,'data.html',{'usern':fpg})
        else:
            return re(request,'otp1.html',{'error':1})   

def payment(request):
    name=request.POST['name']
    email=request.POST['email']
    amount=request.POST['amount']
    api_key='rzp_test_30GfnJDEuxWtiA'
    api_sec='I0rlTzsOrJdqdrzkWibIqkUD'
    print(name,email,amount)
    amount=int(amount)*100
    client = razorpay.Client(auth=(api_key, api_sec))
 
    data = {"amount":amount, "currency": "INR", "receipt": "order_rcptid_11",'payment_capture':1}
    payment = client.order.create(data=data)
    order_id=payment['id']
    d={'name':name,'order_id':order_id,'api_key':api_key,'amount':amount,'email':email}
    return re(request,'razorpay.html',d)