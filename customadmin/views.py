from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import GlobalSettings, Navigation


# Create your views here.
def admin_login(request):
   
    try:
        # messages.info(request, 'Account not found')
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user_obj = User.objects.filter(username=username)

            if not user_obj.exists():
                messages.info(request, "Account not found")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            print(username, password)
            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                messages.success(request, "successfulley logged In.")
                return redirect("dashboard")
            else:
                messages.info(request, "Invalid password")
                return redirect("login")
            

        return render(request, "login.html")

    except Exception as e:
        print(e)
        # Add a proper response in case of an exception
        return HttpResponse("An error occurred")

def dashboard(request):
    return render(request, "dashboard.html")

def Logoutpage(request):
    logout(request)
    return redirect("admin_login")
    
def globalsetting(request):
    glob = GlobalSettings.objects.all()
    try:
        data = GlobalSettings.objects.first()
    except GlobalSettings.DoesNotExist:
        data = None

    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        address = request.POST.get("address")
        facebooklink = request.POST.get("facebooklink") 
        twitterlink = request.POST.get("twitterlink")
        instagram = request.POST.get("instagram")
        linkdinlink = request.POST.get("linkdinlink")
        logo = request.FILES.get("logo")
        brochure = request.FILES.get("brochure")
        brochure_name = request.POST.get("brochure_name")
        if data is None:
            # Create a new GlobalSettings object
            data = GlobalSettings(
                SiteName=name,
                SiteContact=contact,
                SiteAddress=address,
                SiteEmail=email,
                Sitetwitterlink=twitterlink,
                Sitefacebooklink=facebooklink,
                Sitelinkdinlink=linkdinlink,
                Siteinstagram=instagram,    
                brochure_name=brochure_name,
            )
        else:
            # Update existing GlobalSettings object
            data.SiteName = name
            data.SiteContact = contact
            data.SiteAddress = address
            data.SiteEmail = email
            data.Sitetwitterlink = twitterlink
            data.Sitefacebooklink = facebooklink
            data.Sitelinkdinlink = linkdinlink
            data.Siteinstagram = instagram
            data.brochure_name = brochure_name

        if logo:
            # Set the uploaded image to the 'logo' field
            data.logo = logo
        if brochure:
            # Set the uploaded image to the 'logo' field
            data.brochure = brochure
        data.save()

        return redirect(
            "globalsetting"
        )  # Redirect to the same view after saving the data

    return render(request, "globalsetting.html", {"data": data, "glob": glob})


def main_navigation(request, parent_id=None):
    glob = GlobalSettings.objects.all()

    if parent_id:
        obj = Navigation.objects.filter(Parent=parent_id).order_by("position")
    else:
        obj = Navigation.objects.filter(Parent=None).order_by("position")

    return render(
        request,
        "main_navigation.html",
        {"obj": obj, "parent_id": parent_id, "glob": glob},
    )


def navigation_list(request, parent_id=None):
    glob = GlobalSettings.objects.all()
    obj = Navigation.objects.all()

    if request.method == "POST":
        # Retrieve form data
        # next = request.POST.get('next','/')
        name = request.POST.get("name")
        caption = request.POST.get("caption")
        status = request.POST.get("status")
        position = request.POST.get("position")
        page_type = request.POST.get("page_type")
        title = request.POST.get("title")
        short_desc = request.POST.get("short_desc")
        short_desc1 = request.POST.get("short_desc1")
        short_desc2 = request.POST.get("short_desc2")
        short_desc3 = request.POST.get("short_desc3")
        banner_image = request.FILES.get("banner_image")
        brochure = request.FILES.get("brochure")
        meta_title = request.POST.get("meta_title")
        meta_keyword = request.POST.get("meta_keyword")
        icon_image = request.POST.get("icon_image")
        slider_image = request.FILES.get("slider_image")
        parent_id = request.POST.get("Parent")
        desc = request.POST.get("desc")

        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None

        # Create a new Navigation objectj
        obj = Navigation.objects.create(
            name=name,
            caption=caption,
            status=status,
            position=position,
            page_type=page_type,
            title=title,
            short_desc=short_desc,
            short_desc1=short_desc1,
            short_desc2=short_desc2,
            short_desc3=short_desc3,
            meta_title=meta_title,
            meta_keyword=meta_keyword,
            desc=desc,
            icon_image=icon_image,
            Parent=parent_navigation,  # Assign parent navigation object
        )
        # obj.Parent = Navigation.objects.filter(id=parent_id)

        # Set uploaded images
        if banner_image:
            obj.banner_image = banner_image
        if slider_image:
            obj.slider_image = slider_image
        if brochure:
            obj.brochure = brochure

        obj.save()  # Save the new Navigation object to the database

        obj = Navigation.objects.all()  # Update the navigation list with the new object

        if parent_id:
            return redirect("main_navigation", parent_id=parent_id)
        else:
            return redirect("main_navigation")

    return render(
        request, "navigation.html", {"obj": obj, "glob": glob, "parent_id": parent_id}
    )


def update(request, pk):
    glob = GlobalSettings.objects.all()
    data = get_object_or_404(Navigation, pk=pk)

    if request.method == "POST":
        name = request.POST.get("name")
        caption = request.POST.get("caption")
        status = request.POST.get("status")
        position = request.POST.get("position")
        page_type = request.POST.get("page_type")
        title = request.POST.get("title")
        short_desc = request.POST.get("short_desc")
        short_desc1 = request.POST.get("short_desc1")
        short_desc2 = request.POST.get("short_desc2")
        short_desc3 = request.POST.get("short_desc3")
        desc = request.POST.get("desc")
        banner_image = request.FILES.get("banner_image")
        meta_title = request.POST.get("meta_title")
        meta_keyword = request.POST.get("meta_keyword")
        icon_image = request.POST.get("icon_image")
        slider_image = request.FILES.get("slider_image")
        brochure = request.FILES.get("brochure")
        parent_id = request.POST.get("Parent")
        videolink = request.POST.get("videolink")

        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None

        # Update the object with the form data
        data.name = name
        data.caption = caption
        data.status = status
        data.position = position
        data.page_type = page_type
        data.title = title
        data.short_desc = short_desc
        data.short_desc1 = short_desc1
        data.short_desc2 = short_desc2
        data.short_desc3 = short_desc3
        data.meta_title = meta_title
        data.meta_keyword = meta_keyword
        data.desc = desc
        data.Parent = parent_navigation
        data.icon_image = icon_image
        data.videolink = videolink

        if banner_image:
            data.banner_image = banner_image

        if slider_image:
            data.slider_image = slider_image

        if brochure:
            data.brochure = brochure

        data.save()

        if parent_id:
            return redirect("main_navigation", parent_id=parent_id)
        else:
            return redirect("main_navigation")

    parent_id = data.Parent.id if data.Parent else None

    return render(
        request, "update.html", {"data": data, "glob": glob, "parent_id": parent_id}
    )


def delete_nav(request, pk):
    obj = get_object_or_404(Navigation, pk=pk)
    parent_id = None

    if request.method == "POST":
        parent_id = obj.Parent.id if obj.Parent else None
        obj.delete()

    if parent_id:
        return redirect("main_navigation", parent_id=parent_id)
    else:
        return redirect("main_navigation")