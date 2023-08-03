from django.shortcuts import render
from django.http import HttpRequest, response, HttpResponse
from .models import FibNum
from fibonacci_generator.fibonacci_series import fibonacci_series
# Create your views here.


def user_input(request):
    if request.method == "POST":
        nth_term = int(request.POST['n_term'])
        data = FibNum.objects.all()
        # data.delete()
        max_n = float('-inf')

        for i in data:
            max_n = max(i.n, max_n)

        results = []
        if nth_term <= max_n:
            for n_val in data:
                if n_val.n <= nth_term:
                    results.append(n_val.value)
                else:
                    break
        elif (nth_term > max_n) and (max_n != float('-inf')):
            n1 = data[max_n-2].value
            n2 = data[max_n-1].value
            n = nth_term - max_n
            for n_val in data:
                results.append(n_val.value)
            results.extend(fibonacci_series(n, n1, n2))
            for val in range(max_n+1, nth_term+1):
                values = FibNum(n=val, value=results[val-1])
                values.save()

        else:
            results = fibonacci_series(nth_term,0,1)
            for val in range(0, nth_term):
                values = FibNum(n=val+1, value=results[val])
                values.save()

        return render(request, 'fibonacci_output.html', {'fib_values':results, 'nth_term':nth_term})
    return render(request, 'user_input.html')


def display_output(request):
    return render(request, 'fibonacci_output.html')




