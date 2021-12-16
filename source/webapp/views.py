from django.shortcuts import render


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def make_calculation_view(request):
    if request.method == 'GET':
        return render(request, 'make_calculation.html')
    else:
        operation = request.POST.get('radioButton')
        result = 0
        first = int(request.POST.get('first'))
        second = int(request.POST.get('second'))
        if operation == '+':
            result = first + second
        elif operation == '-':
            result = first - second
        elif operation == '*':
            result = first * second
        elif operation == '/':
            result = first / second

        context = {
            "first": first,
            "second": second,
            "result_my": result,
            "operation": operation
        }

        return render(request, 'calculation_view.html', context)


