# core/views.py
from django.shortcuts import render
from .forms import CompanyForm
import requests

def check_company(request):
    status = None
    form = CompanyForm(request.POST or None)  # Form ko POST ya empty initialize

    if request.method == 'POST' and form.is_valid():
        company = form.save(commit=False)
        if company.website:
            try:
                response = requests.get(company.website, timeout=5)
                if response.status_code == 200:
                    company.is_verified = True
                    status = "Company seems REAL ✅"
                else:
                    status = "Company website not reachable ⚠️"
            except:
                status = "Company website not reachable ⚠️"
        else:
            status = "No website provided. Cannot verify ❌"
        company.save()

    # **Hamesha render return karo**
    return render(request, 'core/check_company.html', {'form': form, 'status': status})
