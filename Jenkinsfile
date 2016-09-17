node {
    stage("Checkout") {
        checkout scm
    }

    stage("Install Dependencies") {
        sh "virtualenv venv"
        env.WORKSPACE = pwd()
        env.PATH="${env.WORKSPACE}/venv/bin:/usr/bin:${env.PATH}"
        sh ". venv/bin/activate"
        sh "pip install -r requirements.txt"
    }

    stage("Test") {
        sh "python runtests.py"
    }
}
