pipeline {
  agent any
    stages {
      stage('Clone Repository') {
        steps {
        git url: 'https://github.com/vaishnavivoore/exam-c6.git', branch: 'main'
        }
      }

      stage('Build Docker Image') {
        steps {
          bat 'docker build -t exam-c6:v1 .'
        }
      }

      stage('Run Docker Container') {
        steps {
          bat 'docker rm -f exam-c6-container || exit 0'
          bat 'docker run -d -p 5000:5000 --name exam-c6-container exam-c6:v1'
        }
      }
  }
}
