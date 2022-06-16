# Deployment

[Django File Structure](../Django/file-structure.md)  
[Django File Structure](../Django-File-Structure.md)  

**My Project Deployment Process :**  
1. Git pull repository
2. Apply changes in local
3. Git add, commit, push
4. Pushed changes will updated in Git
5. With git repository update jenkins pipeline will be trigger 
6. in Jenkins artifactory will be created 
7. Copy link from jenkins
8. Goto AWS EC2 - kill existing docker image and pull new artifactory image and runserver

