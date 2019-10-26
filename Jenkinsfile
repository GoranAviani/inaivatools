#!groovy

node {

    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            
        stage 'Update Python Modules'
            // Create a virtualenv in this folder, and install or upgrade packages
            // specified in requirements.txt; https://pip.readthedocs.io/en/1.1/requirements.html
            sh 'virtualenv env && source env/bin/activate && pip3 install --upgrade -r requirements.txt'
  


        stage 'Test'
            // Invoke Django's tests
            sh 'source env/bin/activate && python ./manage.py test'
        
        stage 'Deploy'
            sh './deployment/deploy_prod.sh'

        
           
    }

    catch (err) {
        
        throw err
    }

}