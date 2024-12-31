pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'docker build -t jenkins-demo .'
            }
        }
        stage('Unit Test') {
            steps {
                echo 'Running unit tests...'
                // Add a test script here if needed
            }
        }
        stage('Docker Push') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker tag jenkins-demo mydockerhubuser/jenkins-demo:latest'
                    sh 'docker push mydockerhubuser/jenkins-demo:latest'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
                // Add deployment steps here
            }
        }
    }
}
