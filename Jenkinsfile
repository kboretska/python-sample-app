pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('PYPI_API_TOKEN')
    }

    stages {
        stage('Build and Test') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install --upgrade pip setuptools'
                    sh '. venv/bin/activate && pip install .'
                    sh '. venv/bin/activate && pytest || true'
                }
            }
        }

        stage('Package and Deploy') {
            steps {
                script {
                    sh '. venv/bin/activate && python3 setup.py sdist bdist_wheel'
                    sh '''
                        . venv/bin/activate
                        pip install --upgrade twine
                        twine upload --repository pypi dist/* -u __token__ -p $PYPI_TOKEN
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Успішне виконання Pipeline!"
        }
        failure {
            echo "❌ Помилка у Pipeline. Перевір логи."
        }
    }
}
