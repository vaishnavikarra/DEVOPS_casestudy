pipeline{
    agent any
    stages{
        stage ("Build Docker Image"){
            steps{
                echo "Build Docker Image"
                bat "docker build -t kubeapp:v2 ."
            }
        }
        stage ("Docker Login"){
            steps{
                bat "docker login -u vaishnavikarra -p Harekrishna8*"
            }
        }
        stage("push Docker Iamge to Docker Hub"){
            steps {
                echo "push Docker Image to docker hub"
                bat "docker tag kubeapp:v2 vaishnavikarra/newssearch:latest"
                bat "docker push vaishnavikarra/newssearch:latest"


            }
        }
        stage("Deploy to Kubernetes"){
            steps{
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed scucessfull!'

        }
        failure{
            echo "Pipeline failed.Please check the logs."
        }
    }
}
