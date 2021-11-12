def plural_form(value, form1, form2, form5):
    n = abs(value) % 100
    n1 = n % 10
    result_form = form5
    if 10 < n < 20:
        result_form = form5
    elif 1 < n1 < 5:
        result_form = form2
    elif n1 == 1:
        result_form = form1
    return f'{result_form}'
