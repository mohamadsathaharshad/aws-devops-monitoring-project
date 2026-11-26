pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking source code'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask Application'
                sh 'docker --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Flask Application'
                sh 'python3 --version'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker Image'
                sh 'docker build -t flask-devops-app:latest .'
            }
        }

    }

    post {
        success {
            echo 'Pipeline Completed Successfully!'
        }

        failure {
            echo 'Pipeline Failed! Check Console Output.'
        }
    }
}
