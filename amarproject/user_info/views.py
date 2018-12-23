from django.shortcuts import render

# Create your views here.


def show_user_info(request):

    if request.method == 'POST':
        user_name_value = request.POST["user_name"]
        print("Your user name is ", user_name_value)
        return render(request, 'user_info/user_info.html', {"name": user_name_value})
    context = {}
    return render(request, 'user_info/user_info.html', context)
