```
    node(label:'docker') {

    def exception_msg 
    props = readProperties  file:"Jenkins.properties"
	def tag = props['tag']
	def pom_version
	def img
	def environment
	def namespace
	def deploymentname
	def values  
	def profile
	def package_url
		
	try{

        stage("Checkout") {
                checkout scm
        }

        stage('Docker Build') {
           echo "create docker image"
           println(env.BRANCH_NAME)
           //env.BRANCH_NAME = 'prod'  //should be in lower case!!
           if (env.BRANCH_NAME == 'master'){
                namespace = 'prod'
                tag='22.05.10'
                package_url = "artifacts.abc.org/docker-local/cm_northbound/awstools/" + namespace
                img = docker.build("${package_url}")
                img.tag("${tag}")
           }
           if (env.BRANCH_NAME == 'dev'){
                namespace = 'dev'
                tag='21.6.42'
                package_url = "artifacts.abc.org/docker-local/cm_northbound/awstools/" + namespace
                img = docker.build("${package_url}")
                img.tag("${tag}")
           }
        }

        stage('Docker Push') {
                echo "push docker image to artifacts"
                
                docker.withRegistry('https://artifacts.abc.org', 'artifacts.abc.org') {
                img.push("${tag}") // Pushing the image
                }
                currentBuild.result = 'SUCCESS'
            }

   }catch(err) {
        println(err.toString())
        error(err.getMessage())
		currentBuild.result = 'FAILED'
		exception_msg = err.getMessage();
		 } finally {
        stage('Clean Workspace') {
            cleanWs()
            }
             
  }
 }
```
