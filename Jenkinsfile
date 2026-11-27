pipeline {

    agent any

    environment {
        DOCKERHUB_REPO = 'mohamadsathaharshad/new-flask-app'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking GitHub source code'

                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies'

                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Flask Application Tests'

                sh '.venv/bin/pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker Image'

                sh '''
                    docker build \
                    -t $DOCKERHUB_REPO:$BUILD_NUMBER \
                    -t $DOCKERHUB_REPO:latest .
                '''
            }
        }

        stage('Docker Hub Push') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                        -u "$DOCKER_USER" --password-stdin

                        docker push $DOCKERHUB_REPO:$BUILD_NUMBER

                        docker push $DOCKERHUB_REPO:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Deploying Flask Application'

                sh '''
                    docker rm -f flask-devops-app || true

                    docker run -d \
                    --name flask-devops-app \
                    -p 5000:5000 \
                    $DOCKERHUB_REPO:$BUILD_NUMBER
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Checking Application'

                sh '''
                    sleep 5

                    docker ps

                    curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline Completed Successfully!'
        }

        failure {
            echo 'CI/CD Pipeline Failed! Check Console Output.'
        }
    }
}
