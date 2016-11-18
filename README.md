[![Build Status](https://travis-ci.org/Mo-Talha/Nomad.svg?branch=master)](https://travis-ci.org/Mo-Talha/Nomad)
[![Requirements Status](https://requires.io/github/Mo-Talha/Nomad/requirements.svg?branch=master)](https://requires.io/github/Mo-Talha/Nomad/requirements/?branch=master)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

# Nomad

Jobmine statistics on employers and employees.

## Statistics
- Show employer & employer jobs popularity (by # of applicants)
- Show how many spots the employer usually has and how many of them usually get filled (some employers advertise a lot more positions than they hire)
- Show warnings for employer
- Rating for each employer
- Show keywords for each job (Ex. software jobs: programming languages)
- Comment section crawled from ratemycoopjob.com
- Google maps location of most probable location (for employer)
- Allow user to input jobs that they are interested in (either by job title, keywords etc.) and mail them jobs they might be interested in

db.getCollection('job').find({$text: {$search: "Software engineering"}}, {score: {$meta: "textScore"}}).sort({score:{$meta:"textScore"}})