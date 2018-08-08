# Django-polymorphic bug PoC

admin login: `admin`
password: `admin`

Error when trying to delete Order whose first payment has relations:

```
Environment:


Request Method: POST
Request URL: http://localhost:8000/admin/spikeapp/order/

Django Version: 2.0.1
Python Version: 3.6.6
Installed Applications:
['django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'spikeapp.apps.SpikeappConfig',
 'polymorphic']
Installed Middleware:
['django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware']



Traceback:

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/core/handlers/exception.py" in inner
  35.             response = get_response(request)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/core/handlers/base.py" in _get_response
  128.                 response = self.process_exception_by_middleware(e, request)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/core/handlers/base.py" in _get_response
  126.                 response = wrapped_callback(request, *callback_args, **callback_kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/options.py" in wrapper
  574.                 return self.admin_site.admin_view(view)(*args, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/utils/decorators.py" in _wrapped_view
  142.                     response = view_func(request, *args, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/views/decorators/cache.py" in _wrapped_view_func
  44.         response = view_func(request, *args, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/sites.py" in inner
  223.             return view(request, *args, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/utils/decorators.py" in _wrapper
  62.             return bound_func(*args, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/utils/decorators.py" in _wrapped_view
  142.                     response = view_func(request, *args, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/utils/decorators.py" in bound_func
  58.                 return func.__get__(self, type(self))(*args2, **kwargs2)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/options.py" in changelist_view
  1596.                 response = self.response_action(request, queryset=cl.get_queryset(request))

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/options.py" in response_action
  1330.             response = func(self, request, queryset)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/actions.py" in delete_selected
  36.         queryset, opts, request.user, modeladmin.admin_site, using)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/utils.py" in get_deleted_objects
  131.     collector.collect(objs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/utils.py" in collect
  195.             return super().collect(objs, source_attr=source_attr, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/deletion.py" in collect
  222.                         field.remote_field.on_delete(self, field, sub_objs, self.using)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/deletion.py" in CASCADE
  16.                       source_attr=field.name, nullable=field.null)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/utils.py" in collect
  195.             return super().collect(objs, source_attr=source_attr, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/deletion.py" in collect
  218.                     sub_objs = self.related_objects(related, batch)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/contrib/admin/utils.py" in related_objects
  200.         qs = super().related_objects(related, objs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/deletion.py" in related_objects
  234.             **{"%s__in" % related.field.name: objs}

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/query.py" in filter
  836.         return self._filter_or_exclude(False, *args, **kwargs)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/query.py" in _filter_or_exclude
  854.             clone.query.add_q(Q(*args, **kwargs))

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/sql/query.py" in add_q
  1253.         clause, _ = self._add_q(q_object, self.used_aliases)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/sql/query.py" in _add_q
  1277.                     split_subq=split_subq,

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/sql/query.py" in build_filter
  1187.             self.check_related_objects(join_info.final_field, value, join_info.opts)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/sql/query.py" in check_related_objects
  1053.                     self.check_query_object_type(v, opts, field)

File "/home/riton/git/enioka/spike2/.venv/lib/python3.6/site-packages/django/db/models/sql/query.py" in check_query_object_type
  1033.                     (value, opts.object_name))

Exception Type: ValueError at /admin/spikeapp/order/
Exception Value: Cannot query "$0.00": Must be "SepaPayment" instance.
```
