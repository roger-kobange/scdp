import os
import sys
import webbrowser
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mon_projet.settings')
    
   # Check if running under PyInstaller
    if getattr(sys, 'frozen', False):
        # Remove the `runserver` argument if present
        args = sys.argv[1:]
        if 'runserver' in args:
            args.remove('runserver')
        
        # Add the necessary arguments
        args = ['manage.py', 'runserver', '--noreload'] + args
    else:
        args = sys.argv
    
    execute_from_command_line(args)

    # Open the default web browser
    webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    main()
