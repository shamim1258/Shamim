    import boto3
    import smtplib
    import logging
    import cx_Oracle as cx
    import os
    from os import path
    import datetime, csv
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
    from email.mime.text import MIMEText

    class DatabaseOperation():
        def __init__(self):
            self.error_flg = None
            self.output = []
            self.db_conn = None
            self.db_host = None
            self.db_service = None
            self.db_username = None
            self.db_password = None
            self.db_conn_type = None
            self.safemail_host = None
            self.safemail_username = None
            self.safemail_password = None
            self.safemail_from = None

            self.param_base_path = '/kpn/siebel/mufasa/production/'
            self.read_parameter_values()

            d = datetime.datetime.now()

            self.output_file_name = 'Cancel_Order-' + d.strftime("%d_%m_%Y_%H_%M_%S") + ".csv"
            self.output_file_basepath = '/code/aws_tools/cancel_order/Output/'  # Server
            #Local
            # self.output_file_basepath = "C:\\Users\\khan530\\Desktop\\Docs\\Git_Repository\\Deploy_Asset_Status\\Local\\aws_tools\\aws_tools\\cancel_order\\Output\\"

            if self.db_conn_type == 'sid':
                dsn_tns = cx.makedsn(self.db_host, '1521', sid=self.db_service)  # non-prod
            else:
                dsn_tns = cx.makedsn(self.db_host, '1521', service_name=self.db_service)  # production

            self.connection = cx.connect(user=self.db_username, password=self.db_password, dsn=dsn_tns)

        # Get parameter details in AWS SSM
        def __del__(self):
            self.connection.close()

        def read_parameter_values(self):
            logging.info('Reading Parameters from AWS Parameter Store')
            try:
                session = boto3.Session(region_name='eu-west-1')
                ssm = session.client('ssm')
                nxt_tkn = ' '
                resources = None
                while nxt_tkn is not None:
                    ssm_details = ssm.get_parameters_by_path(Path=self.param_base_path, NextToken=nxt_tkn, WithDecryption=True)
                    for param in ssm_details['Parameters']:
                        param_path = param['Name']  # e.g. /kpn/siebel/mufasa/production/db-host
                        param_value = param['Value']
                        if 'db-host' in param_path:
                            self.db_host = param_value
                        elif 'db-service' in param_path:
                            self.db_service = param_value
                        elif 'db-username' in param_path:
                            self.db_username = param_value
                        elif 'db-password' in param_path:
                            self.db_password = param_value
                        elif 'db-connection-type' in param_path:
                            self.db_conn_type = param_value
                        elif 'safemail-host' in param_path:
                            self.safemail_host = param_value
                        elif 'safemail-username' in param_path:
                            self.safemail_username = param_value
                        elif 'safemail-password' in param_path:
                            self.safemail_password = param_value
                        elif 'safemail-from' in param_path:
                            self.safemail_from = param_value
                    nxt_tkn = ssm_details.get('NextToken', None)
            except Exception as err:
                logging.exception(err)

        def get_single_row_data_from_db(self, select_statement):
            logging.info('Getting record from DB for single row fetch')
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(select_statement)
                    rows = cursor.fetchone()
                    self.output.append(self.error_flg)
                    self.output.append(rows)
                    return self.output
                except self.connection.DatabaseError as e:
                    self.error_flg = True
                    msg = str(e)
                    self.output.append(self.error_flg)
                    self.output.append(msg)
                    return self.output

        def get_data_from_db(self, select_statement):
            logging.info('Getting record from DB for all rows fetch')
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(select_statement)
                    rows = cursor.fetchall()
                    self.output.append(self.error_flg)
                    self.output.append(rows)
                    return self.output
                except self.connection.DatabaseError as e:
                    self.error_flg = True
                    msg = str(e)
                    self.output.append(self.error_flg)
                    self.output.append(msg)
                    return self.output

        def update_database(self, update_statement):
            logging.info('Update the DB record')
            msg = ''
            self.error_flg = None
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(update_statement)
                    self.connection.commit()
                    self.output.append(self.error_flg)
                    msg = 'success'
                    self.output.append(msg)
                    return self.output
                except self.connection.DatabaseError as e:
                    self.error_flg = True
                    msg = str(e)
                    self.output.append(self.error_flg)
                    self.output.append(msg)
                    return self.output

        def update_database_2(self, update_statement_1, update_statement_2):
            logging.info('Update the DB record')
            msg = ''
            self.error_flg = None
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(update_statement_1)
                    cursor.execute(update_statement_2)
                    self.connection.commit()
                    self.output.append(self.error_flg)
                    msg = 'success'
                    self.output.append(msg)
                    return self.output
                except self.connection.DatabaseError as e:
                    self.error_flg = True
                    msg = str(e)
                    self.output.append(self.error_flg)
                    self.output.append(msg)
                    return self.output

        def insert_database(self, insert_statement,arg):
            logging.info('Inserting the record in DB')
            msg = ''
            self.error_flg = None
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(insert_statement,arg)
                    self.connection.commit()
                    self.output.append(self.error_flg)
                    msg = 'success'
                    self.output.append(msg)
                    return self.output
                except self.connection.DatabaseError as e:
                    self.error_flg = True
                    msg = str(e)
                    self.output.append(self.error_flg)
                    self.output.append(msg)
                    return self.output

        # Create output file
        def writeTolog(self, content, user_email):
            output_file_name = self.output_file_name
            output_file = self.output_file_basepath + output_file_name
            header = ['Order Number', 'Order Type', 'Order Status', 'Comment']
            with open(output_file, "w",newline ='') as f:
                writer = csv.writer(f,delimiter=';')
                writer.writerow(header)
                for line in content:
                    writer.writerow(line)
            self.send_email(output_file_name,output_file,user_email)
            return self.output_file_name

        # Send email with attachment
        def send_email(self,file_name, file_path,user_email):
            message = MIMEMultipart("alternative")
            message['From'] = self.safemail_from
            message['To'] = user_email
            message['Subject'] = 'Cancel Order Tool Output'
            text = 'Hello, \n\nPFA the cancel order output file. \n\nRegards,\nSiebel CM MUFASA team\n**This is an auto genertated email.**'
            body_text = MIMEText(text, 'plain')
            part = None
            with open(file_path, "rb") as fil:
                part = MIMEApplication(fil.read(), Name=file_name)

            part['Content-Disposition'] = 'attachment; filename="%s"' % (file_name)
            message.attach(part)
            message.attach(body_text)

            session = smtplib.SMTP(self.safemail_host, 587)  # use gmail with port
            session.starttls()  # enable security
            session.login(self.safemail_username, self.safemail_password)
            session.sendmail(self.safemail_from, user_email, message.as_string())
            session.quit()```
