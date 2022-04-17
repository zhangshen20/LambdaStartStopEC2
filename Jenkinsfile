pipeline {

    agent any

    stages {

        stage('Initialise') {
            steps {
                sh 'make clean; make venv'
                // sh 'make clean'
            }
        }        

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