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

* Run build script
* `build`

* Build script will remove existing local database volume, seed database with questions from _questions_data.py, and set default local users
* ### Local users
* #### username: regular@test.com password: test123
* #### username: admin@test.com password: test123


##Build commands

* ###Load custom commands into environment
* `source environment.sh`
* ###Build the entire project
* `build`
* ###Reload docker image and bundle Vue assets
* `reload`
* ###Transpiple and bundle Vue assets
* `js`
* ###Run Django test suite
* `test`
* ###Enter shell_plus
* `shell`


##Adding new questions
* Import question class into questions/questions/_questions_data.py
* Add question class to the questions list
* Add question class to any related tags (add additional tags, if needed)
* Run: `build`

###JS Testing 
* `test-js`
###To test particular JS test file
`docker-compose exec web yarn jest specs/<file-name>.spec.js`
