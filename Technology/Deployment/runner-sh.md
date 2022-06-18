```
#!/usr/bin/env sh
# Getting static files for Admin panel hosting!


cd /code/aws_tools
python /code/aws_tools/manage.py collectstatic --noinput

python manage.py collectstatic --noinput
pwd
ls -lrt
cp -r /code/aws_tools/templates /usr/local/lib/python3.9/site-packages/django/contrib/admin/
cp -r /code/aws_tools/static /usr/local/lib/python3.9/site-packages/django/contrib/admin/
uwsgi --http "0.0.0.0:${PORT}" --module aws_tools.wsgi --master --processes 4 --threads 2
# uwsgi --http "0.0.0.0:81" --module aws_tools.wsgi --master --processes 4 --threads 2
```
