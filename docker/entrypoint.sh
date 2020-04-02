#!/bin/sh

launch_test() {
  # Run test and coverage.
  python manage.py migrate
  test_result=0
  python -m coverage run manage.py test
  test_result=$?
  python -m coverage report
  return $test_result
}

launch_runserver() {
  # Run django server al port defined.
  mkdir -p /var/tmp/django_cache
  python manage.py createsuperuserwithpassword \
        --username admin \
        --password admin \
        --email admin@example.org \
        --preserve
  python manage.py migrate
  python manage.py makemigrations
  python manage.py runserver "0.0.0.0:${1:-8080}"
}

launch_lint() {
  # Run linter.
  python -m pylint api
}

launch_badge_lint() {
  # Make badge for lint for punctuation defined.
  python -m anybadge -o --value="${1:-0}" pylint
}

case $1 in
  "test") launch_test ;;
  "runserver") launch_runserver $2 ;;
  "lint") launch_lint ;;
  "badge_lint") launch_badge_lint $2 ;;
  *) exec "$@" ;;
esac
