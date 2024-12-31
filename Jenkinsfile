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
        sh 'python3 -m unittest discover -s . -p "test_*.py"'
    }
}
        stage('Docker Push') {
            steps {
             script {
               sh 'docker tag jenkins-demo:latest salaheddinechakk/jenkins-demo:latest'
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker tag jenkins-demo salaheddinechakk/jenkins-demo:latest'
                    sh 'docker push salaheddinechakk/jenkins-demo:latest'
                }
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
