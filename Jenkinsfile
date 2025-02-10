pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('PYPI_API_TOKEN')  // Retrieve Test PyPI API Token from Jenkins
    }

    stages {
        stage('Build and Test') {
            steps {
                echo "Creating virtual environment..."
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip setuptools wheel'

                echo "Installing dependencies..."
                sh '. venv/bin/activate && pip install .'

                echo "Running tests..."
                sh '. venv/bin/activate && pytest || true'
            }
        }

        stage('Package and Deploy') {
            steps {
                echo "Creating Python package..."
                sh '''
                    . venv/bin/activate
                    rm -rf dist/*
                    python setup.py sdist bdist_wheel
                '''

                echo "Uploading package to Test PyPI..."
                sh '''
                    . venv/bin/activate
                    pip install --upgrade twine
                    twine upload --verbose --repository-url https://test.pypi.org/legacy/ dist/* -u __token__ -p $PYPI_TOKEN
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs."
        }
    }
}
