from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.views import LoginView, LogoutView
from .models import Sub, Postt, SavePosts, Commentary, Like, User
from .form import LogIn, Register, ProfilForm, Security, ModForm, PersonalForm
from pathlib import Path
from django.core.files import File
from django.shortcuts import redirect, render


class MyProfil(TemplateView):
    template_name = "user_profils.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        post = Postt.objects.filter(user_s=user)
        s_post = SavePosts.objects.get(user_s=user).saves_posts.all()
        sub = Sub.objects.get(user=user)
        context["followers"] = len(sub.subscribers.all())
        context["follow"] = len(sub.subscribe.all())

        if self.kwargs["name"] == "Posts":
            context["posts"] = post
        elif self.kwargs["name"] == "Saves":
            context["posts"] = s_post
        context["user"] = user
        context["iden"] = 2
        return context


class UserPersonal(TemplateView):
    template_name = "user_setting.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        context["form"] = PersonalForm(initial={"first_name": user.first_name, "last_name": user.last_name})
        context["iden"] = 4
        context["h1"] = "Personal setting"
        return context

    def post(self, request):
        data = request.POST
        user = self.request.user
        user.last_name = data["last_name"]
        user.first_name = data["first_name"]
        user.save()
        return JsonResponse("Changed", safe=False)


class UserMod(TemplateView):
    template_name = "user_setting.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["form"] = ModForm(initial={"email": user.email})
        context["iden"] = 3
        context["h1"] = "Modifications setting"
        return context

    def post(self, request):
        data = request.POST
        user = self.request.user
        user.email = data["email"]
        user.save()
        return JsonResponse("Changed", safe=False)


class UserSecurity(TemplateView):
    template_name = "user_setting.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["form"] = Security()
        context["user"] = user
        context["iden"] = 2
        context["h1"] = "User security"
        return context

    def post(self, request):
        data = request.POST
        user = self.request.user

        if data["psw_1"] == data["psw_2"]:
            user.set_password(data["psw_2"])
            user.save()
            return JsonResponse("Changed", safe=False)
        else:
            return JsonResponse("Error", safe=False)


class UserSetting(TemplateView):
    template_name = "user_setting.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["form"] = ProfilForm(initial={"username": user.username,
                                              "status": user.status,
                                              "my_web": user.my_web})
        context["user"] = user
        context["iden"] = 1
        context["h1"] = "User settings"
        return context

    def post(self, request, **kwargs):
        data = request.POST
        data_f = request.FILES
        user = self.request.user

        if data_f["avatar"]:
            with open("INST/static/img/img_post.png", "wb") as img:
                img.write(data_f["avatar"].read())
            cl = Path("INST/static/img/img_post.png")
            with cl.open(mode="rb") as img:
                cl_file = File(img, name=cl.name)
                user.avatar = cl_file
                user.status = data["status"]
                user.my_web = data["my_web"]
                user.username = data["name"]
                user.save()
            return JsonResponse({"status": " " if user.status is None else user.status, "name": user.username,
                                 "my_web": " " if user.my_web is None else user.my_web, "avatar": user.avatar.url}, safe=False)
        else:
            user.status = data["status"]
            user.my_web = data["my_web"]
            user.username = data["name"]
            user.save()
            return JsonResponse({"status": " " if user.status is None else user.status, "name": user.username,
                                 "my_web": " " if user.my_web is None else user.my_web, "avatar": user.avatar}, safe=False)


class UserSuc(TemplateView):
    template_name = "user_suc.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        data = request.POST
        if data["inp_text"]:
            user = User.objects.filter(username__contains=data["inp_text"])
        else:
            user = []
        suc = render_to_string("schb_suc.html", context={"user_list": user})
        return JsonResponse(suc, safe=False)


class UserProfils(TemplateView):
    template_name = "user_profils.html"

    def post(self, request, **kwargs):
        data = request.POST
        user = User.objects.get(id=self.kwargs["user_id"])
        sub = Sub.objects.get(user=user)
        user_sru = Sub.objects.get(user=self.request.user)

        if self.request.user in sub.subscribers.all():
            sub.subscribers.remove(self.request.user)
            sub.int_sub-=1
            user_sru.subscribe.remove(user)
            return JsonResponse({"my_subscribe": False, "followers": len(sub.subscribers.all()),
                                 "follow": len(sub.subscribe.all())}, safe=False)

        else:
            sub.subscribers.add(self.request.user)
            sub.int_sub+=1
            user_sru.subscribe.add(user)
            return JsonResponse({"my_subscribe": True, "followers": len(sub.subscribers.all()),
                                 "follow": len(sub.subscribe.all())}, safe=False)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.id == self.kwargs["user_id"]:
            return redirect("/Myprofil/Posts")
        else:
            context = {}
            user = User.objects.get(id=self.kwargs["user_id"])
            post = Postt.objects.filter(user_s=user)
            sub = Sub.objects.get(user=user)
            s_post = SavePosts.objects.get(user_s=user).saves_posts.all()
            context["followers"] = len(sub.subscribers.all())
            context["follow"] = len(sub.subscribe.all())
            context["my_subscribe"] = True if self.request.user in sub.subscribers.all() else False

            if self.kwargs["name"] == "Posts":
                context["posts"] = post
            elif self.kwargs["name"] == "Saves":
                context["posts"] = s_post

            context["user"] = user
            context["iden"] = 1
            return render(request, "user_profils.html", context)


class Recomendation(View):

    def post(self, request):
        user = self.request.user
        my_sub = Sub.objects.get(user=user)
        my_list = [i for i in my_sub.subscribers.all() if i not in my_sub.subscribe.all()]

        if len(my_list) != 10:
            for el in my_sub.subscribe.all():
                user_sub = Sub.objects.get(user=el)
                for ele in user_sub.subscribe.all():
                    if ele not in my_sub.subscribe.all() and ele not in my_list:
                        my_list.append(ele)
            if len(my_list) != 10:
                most_sub = [i.user for i in Sub.objects.all().order_by("int_sub")] [-1 -(10 - len(my_list)):]
                my_list.extend(list(most_sub))
        my_list.remove(self.request.user)
        scb = render_to_string("scb_base.html", context={"scb": my_list})
        return JsonResponse(scb, safe=False)


class Home(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        sub = Sub.objects.get(user=user)
        post = Postt.objects.all()
        saves = SavePosts.objects.get(user_s=user)
        my_list = []

        for i in post:
            if i.user_s in sub.subscribe.all():
                post_like = Like.objects.filter(post=i)
                for el in post_like:
                    if el.user_s == user:
                        if i in saves.saves_posts.all():
                            my_list.append([i, len(post_like), 1, 3])
                        else:
                            my_list.append([i, len(post_like), 1, 4])
                        break
                else:
                    if i in saves.saves_posts.all():
                        my_list.append([i, len(post_like), 0, 3])
                    else:
                        my_list.append([i, len(post_like), 0, 4])

        context["my_post"] = my_list
        return context

    def post(self, request):
        data = request.POST
        user = self.request.user

        if "post_id" in data.keys():
            post = Postt.objects.get(id=data["post_id"])
            likes = Like.objects.filter(post=post)
            for el in likes:
                if user == el.user_s:
                    el.delete()
                    return JsonResponse({"like_id": False, "num": len(likes) - 1})
            else:
                like = Like(post=post, user_s=user)
                like.save()
                return JsonResponse({"like_id": True, "num": len(likes) + 1})

        else:
            post_s = Postt.objects.get(id=int(data["save_id"]))
            user_posts = SavePosts.objects.get(user_s=user)

            if post_s in user_posts.saves_posts.all():
                user_posts.saves_posts.remove(post_s)
                user_posts.save()
                return JsonResponse({"post_save_id": False}, safe=False)
            else:
                user_posts.saves_posts.add(post_s)
                user_posts.save()
                return JsonResponse({"post_save_id": True}, safe=False)


class PostCreate(TemplateView):

    def post(self, request):
        data = request.POST
        filles = request.FILES
        file = open("INST/static/img/img_post.png", "wb")
        file.write(filles["file"].read())
        file.close()
        cl = Path("INST/static/img/img_post.png")
        with cl.open(mode="rb") as img:
            cl_file = File(img, name=cl.name)
            post_obj = Postt(img=cl_file, text=data["text"], user_s=self.request.user)
            post_obj.save()

        return JsonResponse("Complete", safe=False)


class LoginV(LoginView):
    template_name = "login.html"
    form_class = LogIn
    redirect_authenticated_user = True


class PostPage(TemplateView):
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post"
        postts = Postt.objects.get(id=self.kwargs["id"])
        context["name"] = postts
        context["comment_t"] = Commentary.objects.filter(post=postts)
        context["int"] = len(Like.objects.filter(post=postts))
        for el in Like.objects.filter(post=postts):
            if self.request.user == el.user_s:
                context["like"] = "dislike"
                break
        else:
            context["like"] = "like"

        return context

    def post(self, request, **kwargs):
        data_p = request.POST
        post = Postt.objects.get(id=self.kwargs["id"])

        if "text_c" in data_p.keys():
            text = data_p["text_c"]
            if text == "":
                return JsonResponse("<p class='text-white'>Error</p>", safe=False)
            else:
                comment_d = Commentary(text=text, post=post, user_s=self.request.user)
                comment_d.save()
                html_d = render_to_string("comment_templete.html", context={"user": self.request.user, "comment": comment_d})
                return JsonResponse(html_d, safe=False)

        elif "likes_t" in data_p.keys():
            like = Like.objects.filter(post=post)
            for el in like:
                if self.request.user == el.user_s:
                    el.delete()
                    return JsonResponse({"ection": "like", "int": len(like)-1})
            else:
                liked = Like(post=post, user_s=self.request.user)
                liked.save()
                return JsonResponse({"ection": "dislike", "int": len(like)+1})


class Registration(CreateView):
    template_name = "register.html"
    form_class = Register

    def get_success_url(self):
        a = self.object
        sub = Sub(user=a)
        sub.save()
        post_save = SavePosts(user_s=a)
        post_save.save()
        return "/Login"


class Logout(LogoutView):
    pass