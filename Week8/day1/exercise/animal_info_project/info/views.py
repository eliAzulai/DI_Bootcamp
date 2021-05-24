from django.shortcuts import render
from .info import families, animals

def family(request, fam_id):
    for family in families:
        if family['id'] == fam_id:
            fam = family
            break
    return render(request, 'family.html', context ={'fam': fam})

def animal(request, animal_id):
    return render(request, 'animal.html', context={})