<div align="center" id="topOfReadme">
	<h1>EOS | Astraeus</h1>
	<em>Generates download links for massive datasets</em></br>


<a href="https://github.com/eos-sns/astraeus/pulls"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a> <a href="https://github.com/eos-sns/astraeus/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a> <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a> <a href="https://www.python.org/download/releases/3.6.0/"><img src="https://img.shields.io/badge/Python-3.6-blue.svg"></a> <a href="https://saythanks.io/to/sirfoga"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanks!" /></a>
</div>


## Use case
You want to share datasets (.txt, .bin, .hdf5 ...) via downloads. You want

- that the download links are available for just a restricted time frame
- to keep track of downloads requests
- secure actual files location (because the files contain (sensitive | important)-content, that crawlers should not index)
- hide the true location of files

## Install
```bash
$ pip install .
```

### Dependencies
```bash
$ $(which pkg manager) install memcached libmemcached-tools  # install memcache
```

### Upgrade
```bash
$ pip install . --upgrade --force-reinstall
```

## Contributing
[Fork](https://github.com/eos-sns/astraeus/fork) | Patch | Push | [Pull request](https://github.com/eos-sns/astraeus/pulls)

## Feedback
Suggestions and improvements are [welcome](https://github.com/eos-sns/astraeus/issues)!

## Authors

| [![sirfoga](https://avatars0.githubusercontent.com/u/14162628?s=128&v=4)](https://github.com/sirfoga "Follow @sirfoga on Github") |
|---|
| [Stefano Fogarollo](https://sirfoga.github.io) |

## License
All of the codebases are **[MIT licensed](https://opensource.org/licenses/MIT)** unless otherwise specified.

**[Back to top](#topOfReadme)**
