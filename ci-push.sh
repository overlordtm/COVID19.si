#/bin/sh

REPO="github.com/overlordtm/COVID19.si"
FILES="data/full.csv"

git remote add origin https://${GITHUB_TOKEN}@.git


setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit() {
  git checkout master
  git add ${FILES}
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

push() {
  git remote add upstream https://${GH_TOKEN}@${REPO}.git > /dev/null 2>&1
  git push --quiet upstream master
}

setup_git
commit
push