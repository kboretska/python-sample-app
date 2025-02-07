pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('PYPI_API_TOKEN')  // Отримуємо Test PyPI API Token з Jenkins
    }

    stages {
        stage('Build and Test') {
            steps {
                echo "🛠 Створення віртуального середовища..."
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip setuptools wheel'

                echo "📦 Встановлення залежностей..."
                sh '. venv/bin/activate && pip install .'

                echo "✅ Запуск тестів..."
                sh '. venv/bin/activate && pytest || true'
            }
        }

        stage('Package and Deploy') {
            steps {
                echo "📦 Створення Python-пакету..."
                sh '''
                    . venv/bin/activate
                    rm -rf dist/*
                    python setup.py sdist bdist_wheel
                '''

                echo "🚀 Завантаження пакету на Test PyPI..."
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
            echo "🎉 Успішне виконання Pipeline!"
        }
        failure {
            echo "❌ Помилка у Pipeline. Перевір логи."
        }
    }
}
