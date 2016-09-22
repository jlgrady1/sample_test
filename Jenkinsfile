testFiles = ["tests/unit", "tests/integration"]
stage "Starting Build"
node {
    echo "Starting"
}

stage "Test"
def branches = [:]
for (int i = 0; i < testFiles.size(); i++) {
    branches[testFiles[i]] = {
        node {
            runTests()
        }
    }
}

parallel branches

void runTests(def args) {
    node {
    checkout scm
    installDependencies()
    }
}

void installDependencies() {
    sh "virtualenv venv"
    env.WORKSPACE = pwd()
    env.PATH="${env.WORKSPACE}/venv/bin:/usr/bin:${env.PATH}"
    sh ". venv/bin/activate"
    sh "pip install -r requirements.txt"
}
