pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vaishnavivoore/exam-c6.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Python app...'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt || echo No requirements.txt'
            }
        }


    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
