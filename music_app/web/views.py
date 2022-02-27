from django.shortcuts import render, redirect

from music_app.web.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteProfileForm
from music_app.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('profile create')
    albums = Album.objects.all()
    context = {
        'albums': albums,
        'profile': profile,
    }
    return render(request, 'home-with-profile.html',context)


def add_album(request):
    album = Album.objects.all()
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = AddAlbumForm()

    context = {
        'form': form,

    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
        'profile': profile,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request == 'POST':
        form = EditAlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):

    return render(request, 'delete-album.html')


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    album = Album.objects.all()
    context = {
        'profile': profile,
        'album': album,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
