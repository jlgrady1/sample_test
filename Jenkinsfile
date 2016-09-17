node {
    stage 'Install Dependencies'
    sh 'virtualenv venv'
    sh '. venv/bin/activate'
    sh 'pip install -r requirements.txt'

    stage 'Test'
    sh 'python runtests.py'
}
