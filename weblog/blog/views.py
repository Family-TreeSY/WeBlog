# -*- coding:utf-8 -*-
# from django.shortcuts import render
# from django.http import Http404
# from django.core.paginator import Paginator, EmptyPage
from django.core.cache import cache
from django.views.generic import ListView, DetailView
from silk.profiling.profiler import silk_profile

from .models import Post, Category, Tag
from config.models import SideBar
from comment.models import Comment
# from comment.forms import CommentForm
from comment.views import CommentShowMixin


def cache_it(func):
    def wrapper(self, *args, **kwargs):
        key = repr((func.__name__, args, kwargs))
        result = cache.get(key)
        if result:
            print('Hit cache')
            return result
        print('Hit db')
        result = func(self, *args, **kwargs)
        cache.set(key, result, 60 * 5)
        return result
    return wrapper

class CommonMixin(object):
    @silk_profile(name='get_category_context')
    # @cache_it
    def get_category_context(self):
        """
        分类
        nav_cates = categories.filter(is_nav=True) 导航分类
        cates = categories.filter(is_nav=False)  普通分类
        在modles中is_nav属性是布尔值
        """
        categories = Category.objects.all()
        cates = []
        nav_cates = []
        for category in categories:
            if category.is_nav:
                nav_cates.append(category)
            else:
                cates.append(category)
        return {
            'nav_cates': nav_cates,
            'cates': cates,
        }

    def get_sidebar_data(self):
        """
        侧边栏
        """
        sidebars = SideBar.objects.filter(status=1)
        return {
            'sidebars': sidebars,
        }


    def get_context_data(self, **kwargs):
        hot_posts = Post.objects.filter(status=1).order_by('-pv')[:5]
        recently_posts = Post.objects.filter(status=1)[:5]
        recently_comments = Comment.objects.filter(status=1)[:2]

        kwargs.update({
            # 'posts': queryset
            # 'nav_cates': nav_cates,
            # 'cates': cates,
            # 'sidebars': sidebars,
            'recently_posts': recently_posts,
            'recently_comments': recently_comments,
            'hot_posts': hot_posts,
        })
        kwargs.update(self.get_category_context())
        kwargs.update(self.get_sidebar_data())
        return super(CommonMixin, self).get_context_data(**kwargs)


class BasePostsView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasePostsView):
    '''
        增加搜索功能
        1.数据过滤
        2.数据传递到模板里
        '''

    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super(IndexView, self).get_queryset()
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)

class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostsView):
    def get_queryset(self):
        tag_id  = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            return []

        posts = tag.posts.all()
        return posts

'''
作者搜索页面
'''
class AuthorView(BasePostsView):
    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        qs = super(AuthorView, self).get_queryset()
        if author_id:
            qs = qs.filter(user_id=author_id)
        return qs


class PostView(CommonMixin, CommentShowMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        sessionid = self.request.COOKIES.get('sessionid')
        if not sessionid:
            return

        pv_key = 'pv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 60)

        uv_key = 'uv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60*60*24)


    # def get_comment(self):
    #     target = self.request.path
    #     comments = Comment.objects.filter(target=target)
    #     return comments
    #
    # def get_context_data(self, **kwargs):
    #     kwargs.update({
    #         'comment_form': CommentForm(),
    #         'comment_list': self.get_comment()
    #     })
    #     return super(PostView, self).get_context_data(**kwargs)


#
# def get_common_context():
#     """
#         分类
#         nav_cates = categories.filter(is_nav=True) 导航分类
#         cates = categories.filter(is_nav=False)  普通分类
#         在modles中is_nav属性是布尔值
#         """
#     categories = Category.objects.all()
#     cates = []
#     nav_cates = []
#     for category in categories:
#         if category.is_nav:
#             nav_cates.append(category)
#         else:
#             cates.append(category)
#
#     """
#     侧边栏
#     """
#     sidebars = SideBar.objects.filter(status=1)
#
#     recently_posts = Post.objects.filter(status=1)[:5]
#     recently_comments = Comment.objects.filter(status=1)[:2]
#
#     context = {
#         # 'posts': queryset
#         'nav_cates': nav_cates,
#         'cates': cates,
#         'sidebars': sidebars,
#         'recently_posts': recently_posts,
#         'recently_comments': recently_comments,
#
#     }
#     return context
#
#
# def post_list(request, category_id=None, tag_id=None):
#     '''
#     context: 把参数传递给模板
#     render(): 根据我们传入的参数来构造HttpResponse
#
#     '''
#     # 获取文章列表
#     # order_by: 以逆序时间来获取，博客文章最新建的在最上面
#     queryset = Post.objects.all().order_by('-created_time')
#     if category_id: # 分类页面
#         queryset = queryset.filter(category_id=category_id)
#     elif tag_id: # 标签页面
#         try:
#             tag = Tag.objects.get(id=tag_id)
#         except Tag.DoesNotExist: # 不存在返回[]
#             queryset = []
#         else: # try语句执行成功，运行else语句，tag标签下的文章被显示出来
#             queryset = tag.posts.all()
#     '''
#     分页
#     '''
#     # 从第一页开始
#     page = request.GET.get('page', 1)
#     try:
#         page = int(page)
#     except TypeError:
#         page = 1
#     # 每页三条数据
#     page_size = 3
#     # 创建Paginator实例
#     paginator = Paginator(queryset, page_size)
#     try:
#         posts = paginator.page(page)
#     except EmptyPage: # 超过页码范围就传递最后一页数据
#         posts = paginator.page(paginator.num_pages)

    # """
    # 分类
    # nav_cates = categories.filter(is_nav=True) 导航分类
    # cates = categories.filter(is_nav=False)  普通分类
    # 在modles中is_nav属性是布尔值
    # """
    # categories = Category.objects.all()
    # cates = []
    # nav_cates = []
    # for category in categories:
    #     if category.is_nav:
    #         nav_cates.append(category)
    #     else:
    #         cates.append(category)
    #
    # """
    # 侧边栏
    # """
    # sidebars = SideBar.objects.filter(status=1)
    #
    # recently_posts = Post.objects.filter(status=1)[:5]
    # recently_comments = Comment.objects.filter(status=1)[:2]


#     context = {
#         # 'posts': queryset
#         'posts': posts,
#         # 'nav_cates': nav_cates,
#         # 'cates': cates,
#         # 'sidebars': sidebars,
#         # 'recently_posts': recently_posts,
#         # 'recently_comments': recently_comments,
#
#     }
#     common_context = get_common_context()
#     context.update(common_context)
#     return render(request, 'blog/list.html', context=context)
#
#
# def post_detail(request, pk=None):
#     '''
#
#     :param request:
#     :param pk: post_detail
#     :return:
#     '''
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Http404('Post is not exist!')
#
#     context = {
#         # 'posts': queryset
#         'post': post,
#
#     }
#     common_context = get_common_context()
#     context.update(common_context)
#     return render(request, 'blog/detail.html', context=context)
#
#
