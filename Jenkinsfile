pipeline {
    agent any
   tools{
       gradle 'gradle'
   }
    stages {
        stage('run frontend') {
            steps {
               echo 'build my app'
                nodejs('node-23'){
               sh 'yarn install'
                }
            }
        }

        stage('run backend') {
            steps {
                echo 'Running tests...'
                sh './gradlew -v'
               
            }
        }
    }
}

   

