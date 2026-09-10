pipeline {
    agent any

    stages {
        stage('GitHub') {
            steps {
                git branch: 'main', credentialsId: 'jen-git-dind', url: 'https://github.com/Tejas-dev-prog/-Complete_CICD_02.git'
            }
        }
    }
}
