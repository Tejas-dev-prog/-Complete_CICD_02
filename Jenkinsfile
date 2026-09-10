pipeline {
    agent any
	tools {
	   nodejs 'NodeJS'
	   }
    stages {
        stage('GitHub') {
            steps {
                git branch: 'main', credentialsId: 'jen-git-dind', url: 'https://github.com/Tejas-dev-prog/-Complete_CICD_02.git'
            }
        }
	stage ('Unit Test'){
		steps{
			sh 'npm test'
			sh 'npm install'		     
		      }
	}
    }
}
