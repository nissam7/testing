pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git clone https://github.com/nissam7/testing.git
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t contact-app .'
      }
    }

    stage('Deploy') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}

