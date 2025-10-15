pipeline{
	agent any
	stages{
	stage('checkout'){
	steps{
	echo "Cloning repo"
	git url:"https://github.com/vaishnavikarra/DEVOPS_casestudy.git",
	branch:'master'
	}
	}
	stage('Build'){
	steps{
	echo "Build Docker Image"
	bat "docker build -t newssearch ."
	}
	}
	stage('Run'){
	steps{
	echo "Run application in Docker Container"
	bat "docker rm -f newscontainer || exit 0"
	bat "docker run -d -p 5001:5001 --name mycontainer newsearch"
	}
	}
	}
	post{
	success{
	echo 'Pipeline finished successfully!'
	}
	failure{
	echo 'Pipeline failed.Please check the logs'
	}
	
	}
}
