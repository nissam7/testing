pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/nissam7/testing.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t html-site .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f html-container || true
                docker run -d -p 8081:80 --name html-container html-site
                '''
            }
        }
    }
}

