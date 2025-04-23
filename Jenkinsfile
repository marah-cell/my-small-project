pipeline {
    agent any

    stages {
        stage('build') {
            steps {
               echo 'build my app'
                nodejs('node-23'){
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

   

