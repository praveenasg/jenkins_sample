pipeline {
    agent any 
    environment {
        registry = "praveenasg/carapp_repo"
        registryCredential = 'Docker'
        dockerImage = ''
    }
    stages {
        stage('git clone') {
            steps {
              git branch: '', url: 'https://github.com/praveenasg/jenkins_sample.git'
            }
        }

    stage('docker build') {
      steps{
        script {
          sh 'docker build -t ${registry}:V${BUILD_NUMBER}'
        }
      }
    }
    
    stage('docker hub') {
     steps{    
         script {
            docker.withRegistry( '', registryCredential ) {
            sh 'docker push ${registry}:V${BUILD_NUMBER}'
            }
        }
      }
    }
  }
}