pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('PYPI_API_TOKEN')  // Store PyPI token securely in Jenkins
    }

    stages {
        stage('Build and Test') {
            steps {
                script {
                    echo "Setting up Python virtual environment..."
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate && pip install --upgrade pip setuptools'

                    echo "Installing dependencies from setup.py..."
                    sh '. venv/bin/activate && pip install .'

                    echo "Running tests..."
                    sh '. venv/bin/activate && pytest --junitxml=report.xml || true'
                }
            }
        }

        stage('Package and Deploy') {
            steps {
                script {
                    echo "Building the package..."
                    sh '. venv/bin/activate && python setup.py sdist bdist_wheel'

                    echo "Uploading to PyPI..."
                    sh '''
                        . venv/bin/activate
                        pip install twine
                        twine upload --repository pypi dist/* -u __token__ -p $PYPI_TOKEN
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed, check logs for details."
        }
    }
}
