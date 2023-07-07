pipeline {
    agent any 
    environment {
        registry = "praveenasg/carapp_repo"
        registryCredential = '3ac713df-c5fd-4eb9-ae82-96fe1815ebb5'
        dockerImage = ''
    }
    
    stages {
        stage('install docker'){
          steps{
            sh 'sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin'
          }
        }
        stage('git clone') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/praveen']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/praveenasg/jenkins_sample.git']]])       
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