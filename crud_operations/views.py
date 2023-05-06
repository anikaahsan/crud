from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import InfoForm
from .models import Info


def create(request):
    queryset=Info.objects.all()
    # if request.method=='POST':
    #     infoform=InfoForm(request.POST or None)
    #     if infoform.is_valid():
    #         infoform.save()


    #     context=dict(form=infoform,
    #                  queryset=queryset)
    #     return render(request,'create.html', context)



    # else:
    infoform=InfoForm()
    context=dict(form=infoform,
                    queryset=queryset)
    return render(request,'create.html', context)



def update(request,pk):
    info=Info.objects.get(pk=pk)
    infoform=InfoForm(instance=info)
    if request.method=="POST":
         infoform=InfoForm(request.POST or None ,instance=info )

         if infoform.is_valid():
                infoform.save()
                return redirect('create')

    context=dict(data=info,
                 form=infoform)
    return render(request,'update.html',context)

def delete(request,pk):
    info=Info.objects.get(pk=pk)
    info.delete()
    return redirect('create')

@csrf_exempt
def create_with_ajax(request):
     if request.method=="POST":
          form=InfoForm(request.POST or None)
          if form.is_valid():
               name=request.POST['name']
               address=request.POST['address']
               phone=request.POST['phone_number']
               infodata=Info(name=name,address=address,phone_number=phone)
               infodata.save()

               stud=Info.objects.values()
               print(stud)
               student_data=list(stud)

               return JsonResponse({'status':'save','student_data':student_data})
          else:
               return JsonResponse({'status':'not saved'})
          
     