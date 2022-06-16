      
FROM python:3
ENV PYTHONUNBUFFERED=1
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_1

# Install cx_Oracle libraries
WORKDIR /opt/oracle
RUN wget \
    https://download.oracle.com/otn_software/linux/instantclient/211000/instantclient-basic-linux.x64-21.1.0.0.0.zip && \
    unzip instantclient-basic-linux.x64-21.1.0.0.0.zip && \
    rm -f instantclient-basic-linux.x64-21.1.0.0.0.zip
RUN cd /opt/oracle/instantclient_21_1 && rm -f *jdbc* *occi* *mysql* *jar* README*
COPY aws_tools/libaio.so.1 /opt/oracle/instantclient_21_1
COPY aws_tools/libaio1 /opt/oracle/instantclient_21_1
RUN echo "/opt/oracle/instantclient_21_1 > /etc/ld.so.conf.d/oracle-instantclient.conf" && \
    ldconfig

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY aws_tools/PROD_DB/db.sqlite3 /code/aws_tools/

RUN python /code/aws_tools/manage.py makemigrations
RUN python /code/aws_tools/manage.py migrate

RUN chmod 777 /code/aws_tools/runner.sh
RUN pip install uwsgi
ENV PORT=8000
EXPOSE 8000
EXPOSE 1521
# Runner script here
CMD ["/code/aws_tools/runner.sh"]
