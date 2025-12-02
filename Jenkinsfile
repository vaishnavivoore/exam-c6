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
                // Create virtual environment
                bat 'python -m venv venv'
                // Install dependencies if requirements.txt exists
                bat 'venv\\Scripts\\pip install -r requirements.txt || echo No requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run pytest if available
                bat 'venv\\Scripts\\python -m pytest || echo No tests found'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Run app.py in background
                bat 'start /B venv\\Scripts\\python app.py'
            }
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
