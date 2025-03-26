pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clean workspace before build
                cleanWs()
                // Checkout code from your repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    python -m pip install pytest pytest-cov
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    python -m pytest tests/ --cov=src --cov-report=term-missing
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                    @echo off
                    
                    REM Remove old build directory if it exists
                    if exist build rmdir /s /q build
                    
                    REM Create a new build directory
                    mkdir build
                    cd build
                    
                    REM Configure and build the project using PyInstaller
                    python -m PyInstaller --onefile --windowed --clean ^
                        --name SmartCalculator ^
                        --add-data "../imgs/*;imgs/" ^
                        --add-data "../src/*;src/" ^
                        --add-data "../requirements.txt;." ^
                        --specpath "../" ^
                        "../src/Tkinter_Calculator.py"
                    
                    cd ..
                '''
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed!'
        }
        always {
            // Clean up workspace
            cleanWs()
        }
    }
} 