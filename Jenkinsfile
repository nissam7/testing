pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t html-site .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f html-container || true
                docker run -d -p 8080:80 --name html-container html-site
                '''
            }
        }
    }
}

