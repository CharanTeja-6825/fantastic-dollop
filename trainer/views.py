from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

#===============================================Trainer Dashboard View================================================#

def trainer_dashboard(request):
    return render(request, 'trainer/trainer_homepage.html')

def trainer_list(request):
    trainers = User.objects.filter(username__regex=r'^\d{4}$')
    return render(request, 'trainer/trainer_details.html', {'trainers': trainers})

def delete_trainer(request, user_id):
    # Retrieve the user by ID
    trainer = get_object_or_404(User, id=user_id, username__regex=r'^\d{4}$')
    trainer.delete()
    messages.success(request, "Trainer deleted successfully.")
    return redirect('trainer_list')

#=====================================================================================================================#