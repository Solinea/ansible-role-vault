# ansible-role-vault


[![Build Status](https://travis-ci.org/Solinea/ansible-role-vault.svg?branch=master)](https://travis-ci.org/Solinea/ansible-role-vault)

## Purpose:
A simple role to install [Hashicorp's vault](https://www.vaultproject.io/)

## Testing 
This role is instrumented with the [`Molecule`](https://molecule.readthedocs.io/en/stable-1.25/) test harness. To run it, install `Molecule` with pip
```commandline
$ pip install ansible
$ pip install docker
$ pip install molecule==1.2.5
$ pip install testinfra==1.6.4
```
then execute the tests like this
```commandline
$ molecule test 
```
