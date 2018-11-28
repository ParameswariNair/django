from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import pymysql
from django.core.files.storage import FileSystemStorage
# Create your views here.
def mypage(request):
    m="<h1>WELCOME TO DJANGO</h1>"
    return HttpResponse(m)
def mypage2(request):
    data="ccs"
    return render(request,"mypage2.html",{"data":data})
def addNo(request):
    c=""
    if(request.POST):
        a=request.POST.get("fno")
        b=request.POST.get("sno")
        c=int(a)+int(b)
    return render(request,"addno.html",{"c":str(c)})
    
def regform(request):
    con=pymysql.connect("localhost","root","","mydb")
    c=con.cursor()
    if(request.POST):
        Name=request.POST.get("name")
        Address=request.POST.get("address")
        c.execute("insert into reg_table(Name,Address)values('"+Name+"','"+Address+"')")
        con.commit()
    return render(request,"regform.html")

def selectform(request):
    data=""
    con=pymysql.connect("localhost","root","","mydb")
    c=con.cursor()
    
    c.execute("select * from reg_table")
    data=c.fetchall()

    return render(request,"select.html",{"data":data})
   
def registration(request):
    con=pymysql.connect("localhost","root","","newdb")
    c=con.cursor()
    if(request.POST):
       
        Photo=request.FILES["photo"]
        Name=request.POST.get("name")
        Age=request.POST.get("age")
        Gender=request.POST.get("gender")
        Location=request.POST.get("location")
        Email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        role="user"
        if(request.FILES["photo"]): #to save image inside a folder
            myfile = request.FILES["photo"]
            fs = FileSystemStorage()
            path = fs.save(myfile.name,myfile)
        c.execute("insert into registration_tab(ProfilePhoto,Name,Age,Gender,Location,Email,username)values('"+str(Photo)+"','"+str(Name)+"','"+str(Age)+"','"+str(Gender)+"','"+str(Location)+"','"+str(Email)+"','"+str(username)+"')")
        c.execute("insert into login_tab(username,password,role)values('"+username+"','"+password+"','"+role+"')")
        con.commit()


    return render(request,"registration.html")


def login(request):
    data=""
    con=pymysql.connect("localhost","root","","newdb")
    c=con.cursor()
    if(request.POST):
       

        username=request.POST.get("username")
        password=request.POST.get("password")
        d="select * from login_tab where username='"+username+"' and password='"+password+"'"
        c.execute("select * from login_tab where username='"+username+"' and password='"+password+"'")
        data=c.fetchone()
        request.session["sname"] =username
        if(data[1]=="user"):
            return HttpResponseRedirect("users")
        elif(data[1]=="admin"):
            return HttpResponseRedirect("adminpage")
        

    return render(request,"login.html",{"d":data})
def users(request):
     

    sname=request.session.get("sname")
    d="select * from registration_tab where username='"+sname+"'"
    c.execute("select * from registration_tab  where username='"+sname+"'")
    data=c.fetchall()
    return render(request,"users.html",{"d":data})

def admin(request):
    data=""
    con=pymysql.connect("localhost","root","","newdb")
    c=con.cursor()
    c.execute("select * from registration_tab")
    data=c.fetchall()
    return render(request,"adminpage.html",{"d":data})

def delete(request):
    
    uname=request.GET.get("username")
    con=pymysql.connect("localhost","root","","newdb")
    c=con.cursor()
    c.execute("delete from registration_tab where username='"+uname+"'")
    c.execute("delete from login_tab where username='"+uname+"'")
    con.commit()
    return HttpResponseRedirect("adminpage")
