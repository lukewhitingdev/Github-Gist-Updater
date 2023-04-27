import argparse
import json
import os
import requests
from dotenv import load_dotenv

arg_parser = argparse.ArgumentParser("Github-Gist-Updater");

arg_parser.add_argument("-i", "--input");
arg_parser.add_argument("-Oi", "--output_id");
arg_parser.add_argument("-On", "--output_name");
arg_parser.add_argument("-t", "--token");

parsed_args = arg_parser.parse_args();

if ((input_file_path := getattr(parsed_args, "input", None)) == None):
    print("[-i | --input] Not defined, please input as command line argument defining the target file to update the gist with.")
    exit(1);

if ((output_gist_id := getattr(parsed_args, "output_id", None)) == None):
    print("[-Oi | --output_id] Not defined, please input as command line argument defining the github gist id you wish to update.")
    exit(1);

if ((output_gist_name := getattr(parsed_args, "output_name", None)) == None):
    print("[-On | --output_name] Not defined, please input as command line argument defining the github gist file name you wish to update.")
    exit(1);

if((github_token := getattr(parsed_args, "token", None)) == None):
    print("[-e | --env] Not defined, please input as command line argument defining the path to the environment file containg credentials.")
    exit(1);

content = open(input_file_path, 'r').read()
headers = {'Authorization': f'token {github_token}'}
res = requests.patch('https://api.github.com/gists/' + output_gist_id, data=json.dumps({'files':{output_gist_name:{"content":content}}}),headers=headers) 

if res.status_code == 200:
    print("Updated gist.")
else:
    print("Something went wrong whilst updating gist. See below: \n\n")
    print(f"Status: {res.status_code}")
    print(f"JSON Below: \n {res.json()}")
