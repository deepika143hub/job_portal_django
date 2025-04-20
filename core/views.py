from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import ApplicationForm

# Show list of all jobs
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'core/job_list.html', {'jobs': jobs})

# Show detail of a single job
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'core/job_detail.html', {'job': job})

# Apply to a job (only once per user)
@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if Application.objects.filter(user=request.user, job=job).exists():
        return redirect('job_list')  # Already applied

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()

    return render(request, 'core/apply.html', {'form': form, 'job': job})

# Dashboard: Show jobs applied by the user
@login_required
def user_dashboard(request):
    applications = Application.objects.filter(user=request.user).select_related('job')
    return render(request, 'core/dashboard.html', {'applications': applications})

# Optional: Separate "My Applications" page
@login_required
def my_applications(request):
    applications = Application.objects.filter(user=request.user).select_related('job')
    return render(request, 'core/my_applications.html', {'applications': applications})
