# Github-Gist-Updater
Simple program for updating gists on github

## Example Usage

`Github-Gist-Updater.exe -i [INPUT_FILE] -Oi [ID_OF_GIST] -On [FILE_NAME_IN_GIST] --token [GITHUB_TOKEN]`

## Help

### How to get the ID of your gist
1. Navigate to gist on github
2. URL should look like `https://gist.github.com/[USERNAME]/[ID]`
3. Copy ID part from url: `https://gist.github.com/[USERNAME]/[ID]`

## Building Source
1. Setup and activate venv
2. Goto src directory
3. Run `pip install -r ./requirements.txt`
4. Goto deploy directory
5. Run `python build_executable.py`