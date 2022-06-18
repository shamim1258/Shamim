# Deployment

**Links :**  
- [Django File Structure](Django-File-Structure.md)  
- [JenkinsFile](jenkinsfile.md)  
- [DockerFile](dockerfile.md)  

Test

1.  2space
1.  2space
    1.  2space2space
    1.  4space2space
        1.  3rdlevel
        2.  2spaces
    1.  4space2space
1.  4space
1.  4space



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
        4.  By default setting above command will run the [DockerFile](dockerfile.md) from jenkins logs ```[internal] load build definition from Dockerfile```.
        5.  ```docker.withRegistry('https://artifacts.kpn.org', 'artifacts.kpn.org') { img.push("${tag}") // Pushing the image }```  
This line will publish docker build image to the artifactory where withRegistry method takes 1 arguments as customer artifactory url and 2nd argument is the credentials which are coming from Jenkins Credential Manager. ```img.push``` for pushing image with the latest tag.
7. 
8. With git repository update jenkins pipeline will be trigger 
9. in Jenkins artifactory will be created 
10. Copy link from jenkins
11. Goto AWS EC2 - kill existing docker image and pull new artifactory image and runserver

