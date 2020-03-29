pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                sh "make build-all"
            }            
        }
        stage('Package') {
            steps {
                sh "make package-all"
            }
        }
        stage('Deploy') {
            steps {
                sh "make deploy-all"
            }
        }

    }

}