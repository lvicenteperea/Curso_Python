# Overview

* [Usage](#Usage)
  * [windows](#windows)
    * [windows install](#windows-installation)
    * [windows env folders](#windows-env-folders)
    * [windows unit tests](#windows-unit-tests)
    * [windows flake8 linting](#windows-flake8-linting)
    * [windows mypy type checks](#windows-mypy-type-checks)

## Usage

We assume credentials are kept in the `credentials/` directory, which is .gitignored.

Needed credentials:
* `credentials/hubspot_api_key`:[key for hubspot dev account](https://app.hubspot.com/api-key/9000637/call-log)

### windows

**Deploy Full Workflow**:
```
* env\Scripts\python -m vantablack.wrapper^
    --api_key_path credentials\hubspot_api_key^
    --filename joined_data.csv
```
```
Getting Email Ids:
* env\Scripts\python -m vantablack.email_ids_to_file^
    --directory env\emails_directory^
    --api_key_path credentials/hubspot_api_key
```
```
Getting Email Statistics:
* env\Scripts\python -m vantablack.email_statistics_to_directory^
    --directory env\email_statistics^
    --file_ids_path env\emails_directory\emails_ids.json^
    --api_key_path credentials/hubspot_api_key
```
```
Getting Email Events Hubspot:
* env\Scripts\python -m vantablack.email_click_events_to_directory^
    --directory env\email_click_events^
    --directory_ids_path env\email_statistics^
    --api_key_path credentials/hubspot_api_key^
    --eventType CLICK
```
```
Appending
* env\Scripts\python -m vantablack.merging_events_with_emails^
    --directory_emails env\email_statistics^
    --directory_events env\email_click_events^
    --filename joined_data.csv
```
#### windows_installation

1. install virtualenv:
  `python -m venv env`
2. install requirements in virtual env:
  `env\Scripts\pip install -r requirements.txt`
3. you can launch an interpreter in the env context like this:
  `env\Scripts\python`
4. check your creds are correct:
  `env\Scripts\python -m vantablack.email_ids_to_file`

#### windows env folders
For this to run correctly we need 3 env folders:
* **env\email_click_events**
* **env\email_statistics**
* **env\emails_directory**

#### windows unit tests
To run unit tests using the built-in [test discovery mechanism](https://docs.python.org/3/library/unittest.html#unittest-test-discovery), simply run:

```bash
env\Scripts\python -m unittest discover
```

#### windows flake8 linting

Run flake8 on the packages:

```
env\Scripts\python -m flake8 --select F vantablack
```

#### windows mypy type checks

This runs [mypy](http://mypy-lang.org/) static typechecks on the code:

```
env\Scripts\python -m mypy --check-untyped-defs --ignore-missing-imports vantablack
```
