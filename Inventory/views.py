from django.shortcuts import render

# Create your views here.
def homepage(request):
    data={  
        "role":"admin",
        "name":"Sam",
        "age":34,
        "values":{
            "one":1,
            "two":2,
        },
        "numbers":[44,67,87]
        
    }
    


    return render(request,"index.html",data)

def basepage(request):
    return render(request,'base.html')

def contactpage(request):
    return render(request,'contact.html')
