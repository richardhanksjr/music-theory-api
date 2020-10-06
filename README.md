[![Build Status](https://travis-ci.com/richardhanksjr/music-theory-api.svg?token=GGd7VMz2EUJpbdYmYJaf&branch=master)](https://img.shields.io/travis/richardhanksjr/music-theory-api)

[![Coverage Status](https://coveralls.io/repos/github/richardhanksjr/music-theory-api/badge.svg?branch=master)](https://coveralls.io/github/richardhanksjr/music-theory-api?branch=master)

#Music Theory App API

## Getting up and running
* Create a .env file in the root of the project with:
1. SECRET_KEY
2. DEBUG
3. ENVIRONMENT
    * use development for local development
4. DATABASE_NAME
    * Can be anything in local development
5. DATABASE_USER
    * Can be anything in local development
6. DATABASE_PASSWORD
    * Can be anything in local development
    
* Load environment commands/alias
* `source environment.sh`
* Run reload script
* `reload`


##Build commands

* ###Load custom commands into environment
* `source environment.sh`
* ### Reload docker image and bundle Vue assets
* `reload`
* ### Transpiple and bundle Vue assets
* `js`

##Adding new questions
* Create a subclass of questions.questions.Question
* Implement all required methods.
* question_type should return a unique, descriptive string
* Add new question to the questions.feature file.  This will register the question
with the application.
