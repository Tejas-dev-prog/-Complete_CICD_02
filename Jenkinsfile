pipeline {
    agent any
 
    stages {
 
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }
 
        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                    -v /var/lib/docker/volumes/375aad987308866110cf5472cfe5e9ca5732956fb66cb0378761731e1a1f678e/_data/workspace/Complete-CICD-Pipeline:/app \
                    -w /app \
                    python:3.10-slim \
                    sh -c "ls -l requirements.txt && pip install --no-cache-dir -r requirements.txt && pytest -v"
                '''
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t devops-cicd-app:3 .
                '''
            }
        }
 
        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f devops-cicd-app || true
 
                    docker run -d \
                        --name devops-cicd-app \
                        --restart unless-stopped \
                        --network complete_cicd_02_default \
                        -p 5000:5000 \
                        devops-cicd-app:3
                '''
            }
        }
 
        stage('Health Check') {
            steps {
                sh '''
                    sleep 5
                    curl --fail http://localhost:5000/health
                '''
            }
        }
    }
 
    post {
        success {
            echo '========================================='
            echo 'CI/CD PIPELINE SUCCESS'
            echo '========================================='
        }
 
        failure {
            echo '========================================='
            echo 'CI/CD PIPELINE FAILED'
            echo '========================================='
        }
    }
}