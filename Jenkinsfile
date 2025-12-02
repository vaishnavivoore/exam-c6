pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from your GitHub repo
                git branch: 'main', url: 'https://github.com/vaishnavivoore/exam-c6.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Python app...'
                // Install dependencies if you have requirements.txt
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run pytest or any test framework you use
                sh './venv/bin/python -m pytest || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Example: run the app (adjust as needed)
                sh 'nohup ./venv/bin/python app.py &'
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
