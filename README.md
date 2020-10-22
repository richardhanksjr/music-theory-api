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
* ###Update the question fixture file to reflect local db
* `update_fixture`
* ###Update db to match state of question fixture file
* `load_fixture`

##Adding new questions
* Start Docker container using the `reload` command to prepopulate db with fixture data
* Create a subclass of questions.questions.Question
* Implement all required methods.
* question_type should return a unique, descriptive string
* Add new question to the Question model
* Add new question to exsiting tags and create any new tags
* run `update_fixture`

###vue cli and npm commands
* docker-compose up -d --build
* docker-compose exec web <below commands>
    * npm install 
    * npm install -g @vue/cli
    * npm install --save axios vue-axios
        // you can install multiple packages at once like line 59: 
            * npm install -g @vue/cli --save axios vue-axios
    * npm run dev 
        // this compiles your vue code
    
    
        // you can check the version to confirm it's installed. 
        * vue --version
        //should be @vue/cli 4.5.7 or something close to that if much lower run:
        * npm uninstall vue-cli -g 
            then run * npm install -g @vue/cli
        * vue add <my-plugin> 
        ///if you want
        
### vue testing with jest
* docker-compose exec web <below command>
    * npm install -g yarn (then you can confirm installation yarn --version)
    * yarn install
    * yarn add vue-template-compiler vue-jest <<<<< or npm install --save-dev vue-jest vue-template-compiler
    * yarn add --dev jest <<<< or npm install --dev jest
    * yarn add @vue/test-utils
    // Run all tests 
        * yarn jest
    // run specific tests 
        * yarn jest specs/<test-file-name>.spec.js
    
    IMPORTANT NOTE:
        1) run: docker-compose exec web yarn jest specs/test.spec.js
            1a) if you get this error:  
                "FAIL  specs/test.spec.js
                    ● Test suite failed to run

                      Cannot find module 'babel-core'...."
                proceed to step 2).
        2) Navigate here in Project GUI: node_modules/vue-jest/lib/compilers/babel-compiler.js
        3) Change line 1 of babel-compiler.js <<<  const babel = require(‘babel-core’)  >>> to <<<  const babel = require(‘@babel/core’)  >>>
        4) go back to 1), test should now pass. You might need to repeat anytime yarn add is run
        5) If error: 
            5a)   ✕ mount question component (95 ms)

                    ● mount question component

                    PrettyFormatPluginError: plugins[p].test is not a functionTypeError: plugins[p].test is not a function

                         test('mount question component', () => {
                         const wrapper = mount(Question)
                          expect(wrapper.html()).toMatchSnapshot()
                                                 ^
                        })
        6) check node_modules folder for jest-serializer-vue folder
            6a) If not there install above packages with npm instead of yarn and check again
   
           

