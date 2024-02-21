pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM 'H/2 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Etape de build..."
            }
        }
        stage('Test') {
            steps {
                echo "Etape de test.."
                sh '''
                python3 -m unittest number_comparer_test.py
                python3 -m unittest number_guess_scenario_test.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Etape de livraison....'
                sh '''
                echo "Livraison..."
                '''
            }
        }
    }
}