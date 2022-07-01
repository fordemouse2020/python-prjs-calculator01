from django.shortcuts import render

def fnindex(request):
    return render(request, "index.html", context=None)

def fncalc(request):

    try:
        n1 = float(request.POST.get("tbxn1"))
    except:
        n1 = 0

    try:
        n2 = int(request.POST.get("tbxn2"))
    except:
        n2 = 0

    try:
        opr = request.POST.get("cbxop")
    except:
        opr = "+"

    if opr == "+":
        result = n1 + n2
    elif opr == "-":
        result = n1 - n2
    elif opr == "x":
        result = n1 * n2
    elif opr == "/":
        result = n1 / n2
    else:
        result = ""

    context = {"qsn1": n1, "qsn2": n2, "qsresult": result}

    return render(request, "calc.html", context=context)
