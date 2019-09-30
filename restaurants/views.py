from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 

    		"my_list":[

    		{"restaurant_name":"Wok n roll",
    		"food_type":"Chinese & Japanese"},

    		{"restaurant_name":"Freej Suweeleh",
    		"food_type":"Kuwaiti"},

    		{"restaurant_name":"Asha's",
    		"food_type":"Indian"}
    		]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

   "my_object":{

   		"restaurant_name":"Burger King",
    	"food_type":"American"
    	 }

    }
    return render(request, 'detail.html', context)
