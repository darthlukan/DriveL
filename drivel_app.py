#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import pwd
import pprint
import httplib2
import multiprocessing
from subprocess import *
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

class Setup(object):
    
    def __init__(self):
        # Copy your credentials from the APIs Console
        # TODO: This should be in a config file and hashed, then decoded
        # at runtime for security purposes.
        self.CLIENT_ID = 'YOUR_CLIENT_ID'
        self.CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

        # Check https://developers.google.com/drive/scopes for all available scopes
        self.OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

        # Redirect URI for installed apps
        self.REDIRECT_URI = 'http://localhost'
        
        # os.getlogin() is the preferred option, but is not working in Peppermint dev env.
        self.driveDir = '/home/' + pwd.getpwuid(os.getuid()).pw_name + '/Drive/'
        
    def get_scope(self):
        return self.OAUTH_SCOPE
        
    def get_redirect(self):
        return self.REDIRECT_URI

    def get_drive_dir(self):
        return self.driveDir
        
    def set_drive_dir(self):
        if os.path.isdir(self.driveDir):
            return self.driveDir
        else:
            os.mkdir(self.driveDir)
            return self.driveDir

class Login(object):
    
    def __init__(self):
        
        # TODO: Modify to match the code layout in my head. Also, tie to GUI.
        # Run through the OAuth flow and retrieve credentials
        self.flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
        self.authorize_url = self.flow.step1_get_authorize_url()
        print 'Go to the following link in your browser: ' + self.authorize_url
        self.code = raw_input('Enter verification code: ').strip()
        self.credentials = self.flow.step2_exchange(self.code)
        
        # Create an httplib2.Http object and authorize it with our credentials
        self.http = httplib2.Http()
        self.http = credentials.authorize(self.http)

        self.drive_service = build('drive', 'v2', http=self.http)
        
class Files(object):
    
    def __init__(self):
        self.types = {'': ''}
    
    def get_file(self, FILE):
        pass
    
    def get_list(self):
        pass
    
    def test_file(self, FILE):
        pass
    
    def insert(self, FILE):
        # Insert a file (From quickstart)
        # TODO: This is meant to be gleaned from the GUI.
        #media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
        #body = {
        #    'title': 'My document',
        #    'description': 'A test document',
        #    'mimeType': 'text/plain'
        #}
        
        #file = drive_service.files().insert(body=body, media_body=media_body).execute()
        pass                        
        
    def copy(self, FILE):
        pass
    
    def remove(self, FILE):
        pass
    
    def restore(self, FILE):
        pass
    
    def update(self, FILE):
        pass

class DriveApp(object):
    pass

if __name__ == '__main__':
    pass