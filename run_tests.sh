#!/bin/sh

set -e

nosetests -v --with-doctest \
    --with-xunit --xunit-file=xunit.xml \
    --with-coverage --cover-html --cover-html-dir=htmlcov \
    --cover-xml --cover-xml-file=coverage.xml \
    "$@" kube_cd_project/ polls/

#2to3 -j 3 -wn -f all -f idioms -f buffer -f set_literal -f ws_comma api/
autopep8 --in-place --aggressive -r kube_cd_project/ polls/
