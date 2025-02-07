pipeline {
    agent any

    environment {
        PYPI_TOKEN = credentials('PYPI_API_TOKEN')  // Отримуємо PyPI токен з Jenkins
    }

    stages {
        stage('Build and Test') {
            steps {
                script {
                    echo "🛠 Створення віртуального середовища..."
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install --upgrade pip setuptools'

                    echo "📦 Встановлення залежностей..."
                    sh '. venv/bin/activate && pip install .'

                    echo "✅ Запуск тестів..."
                    sh '. venv/bin/activate && pytest || true'  // Додай тести, якщо є
                }
            }
        }

        stage('Package and Deploy') {
            steps {
                script {
                    echo "📦 Створення Python-пакету..."
                    sh '. venv/bin/activate && python3 setup.py sdist bdist_wheel'

                    echo "🚀 Завантаження пакету у PyPI..."
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
