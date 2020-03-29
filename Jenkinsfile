pipeline {

    agent any

    stages {

        stage('Initialise') {
            steps {
                script {
                    sh 'make clean; make venv'
                }
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