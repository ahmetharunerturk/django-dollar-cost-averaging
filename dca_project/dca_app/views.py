from django.shortcuts import render

def calculate_dca(request):
    if request.method == 'POST':
        initial_investment = float(request.POST['initial_investment'])
        monthly_investment = float(request.POST['monthly_investment'])
        yearly_investment = float(request.POST['yearly_investment'])
        years = int(request.POST['years'])

        total_contributions = initial_investment + (monthly_investment * 12 * years) + (yearly_investment * years)
        total_investment = total_contributions
        average_investment = total_investment / (1 + years)

        context = {
            'initial_investment': initial_investment,
            'total_investment': total_investment,
            'total_contributions': total_contributions,
            'average_investment': average_investment,
            'final_portfolio_value': 0,
        }
        return render(request, 'dca_app/calculate_dca.html', context)
    return render(request, 'dca_app/calculate_dca.html')
