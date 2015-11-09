#!/bin/sh

set -e

python3.5 manage.py test polls
autopep8 --in-place --aggressive -r kube_cd_project/ polls/
