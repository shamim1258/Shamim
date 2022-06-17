# Deployment

**Links :**  
[Django File Structure](Django-File-Structure.md)  
[DockerFile](dockerfile.md)  
[JenkinsFile](jenkinsfile.md)  

**My Project Deployment Process :**  
1. Git pull repository.  
```git pull <branch-name>```
2. Make changes in this repo locally.
3. **Pushing local changes to remote in Git**
  - ```git status```
  - ```git add <file-names-space-separated>```
  - ```git commit -m "message-string"```
  - ```git push origin <branch-name>```
4. If step-3 is success verify changes in git cloud/remote.
5. Repository contain one file - [JenkinsFile](jenkinsfile.md) which is configured in jenkins configuration to run this as script file, so for every push on git this file will be executed. So deployment is initiated from within repository only running the script from jenkinsfile.
  - This file is reading parameters from file - 'Jenkins.properties'
  - The stages are the jenkins steps in the pipeline.
  - Stage : Checkout  
    - ```checkout scm``` this line is checking out the git repository.
  - Stage - Docker Build
    - Checks the branch working on ```env.BRANCH_NAME```
    - ```docker.build("${package_url}")``` this line will build the docker image (docker image contains the application file/code along with dependencies).
    - ```docker.withRegistry('https://artifacts.kpn.org', 'artifacts.kpn.org') { img.push("${tag}") // Pushing the image }```  
    This line will publish docker build image to the artifactory where withRegistry method takes 1 arguments as customer artifactory url and 2nd argument is the credentials which are coming from Jenkins Credential Manager. ```img.push``` for pushing image with the latest tag.
7. 
8. With git repository update jenkins pipeline will be trigger 
9. in Jenkins artifactory will be created 
10. Copy link from jenkins
11. Goto AWS EC2 - kill existing docker image and pull new artifactory image and runserver

