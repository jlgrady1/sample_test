testFiles = ["tests/unit", "tests/integration"]
stage "Starting Build"
node {
    echo "Starting"
}

def runTests(String testFile) {
    cmd = {
        node {
            echo "Running on ${testFile}"
            checkout scm
            installDependencies()
            sh "python runtests.py ${testFile}"
        }
    }
    return cmd
}

void installDependencies() {
    sh "virtualenv venv"
    env.WORKSPACE = pwd()
    env.PATH="${env.WORKSPACE}/venv/bin:/usr/bin:${env.PATH}"
    sh ". venv/bin/activate"
    sh "pip install -r requirements.txt"
}

stage "Test"
def branches = [:]
for (int i = 0; i < testFiles.size(); i++) {
    branches[testFiles[i]] = runTests(testFiles[i])
}

parallel branches

