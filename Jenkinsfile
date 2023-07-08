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
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/praveenasg/jenkins_sample.git']]])
            }
        }

    stage('docker build') {
      steps{
        script {
           dockerImage = docker.build registry
        }
      }
    }
    
    stage('docker hub') {
     steps{    
         script {
            docker.withRegistry( '', registryCredential ) {
             dockerImage.push()
            }
        }
      }
    }
  }
}