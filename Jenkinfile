pipeline {
    agent any   // Run on any available agent

    environment {
        APP_NAME = "my-app"
        BUILD_DIR = "build"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from Git
                git branch: 'main', url: 'https://github.com/vaishnavivoore/exam-c6.git'
            }
        }

        stage('Build') {
            steps {
                echo "Building ${registration-form}..."
                sh 'mvn clean package'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying ${APP_NAME}..."
                sh 'scp target/my-app.jar user@server:/opt/apps/'
            }
        }
    }
}
