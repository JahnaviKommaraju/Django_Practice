from django.http import response
from django.http.response import HttpResponseNotFound,Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import challenges
from django.template.loader import render_to_string

# Create your views here.
#reverse()->allows us to create paths by referencing to the name of urls
def index_jan(request):
    return HttpResponse('it is January')

def index_feb(request):
    return HttpResponse('it is February')

def every_month(request,month):
    if month=='march':
        return HttpResponse('it is March')
    if month=='april':
        return HttpResponse('it is April')
    if month=='may':
        return HttpResponse('it is May')
    
    else:
        return HttpResponseNotFound('This month is not supported')

month_dict={
        'jan':'this is jan',
        'feb': 'this is feb',
        'march':'this is march',
        'april':'it is April',
        'may':'it is May',
        'june': 'it is june',
        # 'july': 'it is july',
        'july':None,
        'aug':'it is aug',
        'sept': 'it is sep',
        'oct':'it is oct',
        'nov':'it is nov',
        # 'dec': 'it is dec',
        'dec':None
    }

def num_months(request,month):
    all_months=list(month_dict.keys())
    if month>len(all_months):
        return HttpResponse('Invalid month')
    redirect_month=all_months[month-1]
    # return HttpResponseRedirect('/challenges/'+ redirect_month)  
    # #-> here, we are hardcoding the path and if we want to change the url name then we have to change in multiple locations. so to avoid that we use reverse()
    #####for redirecting always use reverse()########
    redirect_path=reverse('month_info',args=[redirect_month]) # /challenges/january here, args is a array/list of dynamic values
    return HttpResponseRedirect(redirect_path)

def get_months(request,month):
    try:
        # months=month_dict[month]   #  }  without using html tags
        # return HttpResponse(months)#  }
        months_text=month_dict[month]
        #response_data=f"<h1>{months_text}</h1>"  #using string interpolation-> this is hardcoding(doing manually)
        ######using render_to_string we can render the templates#######
        # response_data=render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data) 
        ####django supports render() for above statement=> render(request,template)
        return render(request,'challenges/challenge.html',{
            "month":months_text,
            "month_name": month.capitalize()
            })  
    except:
            ###########using HttpResponseNotFound#############
        # return HttpResponseNotFound('<h1>this month is not supported!</h1>') 
            ##########using render_to_string and HttpResponseNotFound##########
        # response_data=render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
            ##########using Http404()##########
        raise Http404()
        

def home_page(request):
    list_items=""
    months=list(month_dict.keys())
    # for month in months:
    #     month_name=month.capitalize()
    #     month_path=reverse('month_info',args=[month])
    #     list_items+=f"<li><a href=\'{month_path}\'>{month_name}</a></li>"
    # ##after for loop list_items will be
    # ###"<li><a href="..">Jan</a><li><a href="..">Feb</a><li><a href="..">March</a>...."
    # response_data=f"<ul><h1>{list_items}</h1></ul>"
    # return HttpResponse(response_data)
    ##using render()
    return render(request,'challenges/index.html',{
        'months':months
    })







    



