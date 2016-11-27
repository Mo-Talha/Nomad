[![Build Status](https://travis-ci.org/Mo-Talha/Nomad.svg?branch=master)](https://travis-ci.org/Mo-Talha/Nomad)
[![Requirements Status](https://requires.io/github/Mo-Talha/Nomad/requirements.svg?branch=master)](https://requires.io/github/Mo-Talha/Nomad/requirements/?branch=master)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

# WaterlooWorks statistics on employers

This project is dedicated to providing students statistical information on employers.

### Installing

To install this project for developing and testing purposes, first install project dependencies.


```
make install
```

Then, install the development or production environment.

```
make devel
```

```
make prod
```

## Virtualenv

We work inside a virtualenv for an isolated environment. Whenever using Python and/or Python dependencies, type 

```
source ~/.virtualenv/Nomad/bin/activate
```

## Running the tests

To run the python tests, simply run 

```
make test
```

## Built With

* [Nginx](https://www.nginx.com/resources/wiki/) - The web server
* [MongoDB](https://www.mongodb.com/) - Database
* [Redis](https://redis.io/) - Caching
* [Elasticsearch](https://www.elastic.co/products/elasticsearch) - Searching
* [NLTK](http://www.nltk.org/) - Natural language processing on job descriptions to generate keywords

## Authors

* **Muhammad Talha** - *Initial work* - [Mo-Talha](https://github.com/Mo-Talha)

See also the list of [contributors](https://github.com/Mo-Talha/Nomad/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [UWFlow](https://github.com/UWFlow/rmc) - For technologies inspiration and code copying :)
* [Codepen.io](http://codepen.io/) - For UI designs
* [Github](https://github.com) - For UI designs