pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t contact-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose down || true
                    docker compose up -d --build
                   '''
            }
        }

    }
}
