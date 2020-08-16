from django.shortcuts import render, redirect
from .forms import DocumentsUpdateForm 
from .models import Member

# Create your views here.
def verify_documents(request, id):
	if request.user.is_authenticated and request.user.role == "volunteer":
		if request.method == 'POST':
			form = DocumentsUpdateForm(request.POST, instance=Member.objects.filter(id=id).first().document.get())
			if form.is_valid():
				form.save()
				# messages.success(request, f'Account update successfully!')
				return redirect('home')

		else:
			form = DocumentsUpdateForm(instance=Member.objects.filter(id=id).first().document.get())    
			context = {
				'form': form,
				'username': Member.objects.filter(id=id).first().user.email,
			}

			return render(request, 'members/document-update.html', context)
	else:
		return redirect('home')

