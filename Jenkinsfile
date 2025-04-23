pipeline {
    agent any

    stages {
        stage('build') {
            steps {
               echo 'build my app'
                nodejs('24'){
               sh 'yarn install'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                withgradle(){
                sh './gradlew -v'
                }
               
            }
        }
    }
}

   

