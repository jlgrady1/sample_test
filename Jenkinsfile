node {
    echo "Starting Build"
}

parallel (
    "stream 1" : {
        node {
            stage("Checkout") {
                checkout scm
            }

            stage("Install Dependencies") {
                installDependencies()
            }

            stage("Test") {
                sh "python runtests.py tests/integration"
            }
        }
    },
    "stream 2" : {
        node {
            stage("Checkout") {
                checkout scm
            }

            stage("Install Dependencies") {
                installDependencies()
            }

            stage("Test") {
                sh "python runtests.py tests/unit"
            }
        }
    }
)


void runTests(def args) {

}

void installDependencies() {
    sh "virtualenv venv"
    env.WORKSPACE = pwd()
    env.PATH="${env.WORKSPACE}/venv/bin:/usr/bin:${env.PATH}"
    sh ". venv/bin/activate"
    sh "pip install -r requirements.txt"
}
