# Deployment

**Links :**  
- [Django File Structure](Django-File-Structure.md)  
- [JenkinsFile](jenkinsfile.md)  
- [DockerFile](dockerfile.md)  

**My Project Deployment Process :**  
1.  Git pull repository.  
    1.  `git pull <branch-name>`.  
2.  Make changes in this repo locally.  
3.  **Pushing local changes to remote in Git**  
    1.  `git status`  
    1.  `git add <file-names-space-separated>`  
    1.  `git commit -m "message-string"`  
    1.  `git push origin <branch-name>`  
4.  If step-3 is success verify changes in git cloud/remote.  
5.  Repository contain one file - [JenkinsFile](jenkinsfile.md) which is configured in jenkins configuration to run this as script file, so for every push on git this file will be executed. So deployment is initiated from within repository only running the script from jenkinsfile.  
    1.  This file is reading parameters from file - 'Jenkins.properties'.  
    2.  The stages are the jenkins steps in the pipeline.  
    3.  Stage Checkout  
        1.  checkout scm This line is checking out the git repository.  
    4.  Stage Docker Build  
        1.  Checks the branch working on `env.BRANCH_NAME`.  
        2.  `docker.build("${package_url}")` this line will build the docker image (docker image contains the application file/code along with dependencies).
        3.  Internally above step will run the command ```docker build -t artifacts.kpn.org/docker-local/cm_northbound/awstools/dev .```
        4.  By default setting above command will run the [DockerFile](dockerfile.md) from jenkins logs ```[internal] load build definition from Dockerfile```. The DockerFile execution explained in step-6 and after executing DockerFile than it will run the below steps.
        5.  ```docker.withRegistry('https://artifacts.kpn.org', 'artifacts.kpn.org') { img.push("${tag}") // Pushing the image }```  
This line will publish docker build image to the artifactory where withRegistry method takes 1 arguments as customer artifactory url and 2nd argument is the credentials which are coming from Jenkins Credential Manager. ```img.push``` for pushing image with the latest tag.
6.  [JenkinsFile](jenkinsfile.md) run the [DockerFile](dockerfile.md) at step 5-iv-c.
    1.  DockerFile download the oracle client for linux library and copy the below 2 files
        - `COPY aws_tools/libaio.so.1 /opt/oracle/instantclient_21_1`
        -  `COPY aws_tools/libaio1 /opt/oracle/instantclient_21_1`
    2.  Copy requirement.txt file to path code/ and run the this file with below command
        -  `RUN pip install -r requirements.txt`
    3.  Coping the db.sqlite3 file from PROD directory
        -  `COPY aws_tools/PROD_DB/db.sqlite3 /code/aws_tools/`
    4.  Running django db migration commands
        -  `RUN python /code/aws_tools/manage.py makemigrations`
        -  `RUN python /code/aws_tools/manage.py migrate`
    5.  Running the [runner.sh](runner-sh.md) file. Will complete step-7 than run below steps.
        -  `CMD ["/code/aws_tools/runner.sh"]`
7.  [runner.sh](runner-sh.md) file is run from step 6-5
    1.  This will load the static files for admin page
        -  `python /code/aws_tools/manage.py collectstatic`
        -  `cp -r /code/aws_tools/templates /usr/local/lib/python3.9/site-packages/django/contrib/admin/`
        -  `cp -r /code/aws_tools/static /usr/local/lib/python3.9/site-packages/django/contrib/admin/`
    2.  Running below command
        -  `uwsgi --http "0.0.0.0:${PORT}" --module aws_tools.wsgi --master --processes 4 --threads 2`
9. With git repository update jenkins pipeline will be trigger 
10. in Jenkins artifactory will be created 
11. Copy link from jenkins
12. Goto AWS EC2 - kill existing docker image and pull new artifactory image and runserver

