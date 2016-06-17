#!/usr/bin/python


################################################################################
#
# Created By : Egbie Uku 
# Name Of The Program : Unzipper.Py 
# Created on the 20/05/2016 at 15:08:15 hrs
# This is version : 2
# Updated on 15th of June 2016
#
#
# File description 
#
# A command line script that contains unzip multiple zips files in a directory.
#
################################################################################


from glob import glob
import zipfile
import os
import optparse
import zipfile
import os

class Unzip(object):
    '''Unzip(class) is class that can unzip multiple files  or a single file in a directory.
    path: The directory path containing the zip files or a the path to a single zip file.
    '''
    def __init__(self, path):
            self._isdir = False
            if path:
                    if os.path.isdir(path):
                            self._isdir = True
                    if self._isdir:
                            self._directory, self._zip_file = path, None  # self._directory = path: extract multiple zip files from a directory
                    else:
                            self._directory, self._zip_file = None, path  # self._zip_file = path: unzip a single zip file.
                    
    def _clean_up(self, z_file_list):
            '''_clean_up(list) -> return(None)
            Cleans the directory of all file .zip extenstions.

            Return     : None
            z_file_list : contains all the zip file extenstion that will
            be removed from the system after clean up.
            '''
            count = 0
            print '\n\n[+] Please wait performing clean up ..\n'
            for zip_file in z_file_list:
                    
                    print '[-] removing zip file ({}) from directory '.format(os.path.basename(zip_file))
                    try:
                            os.remove(zip_file)
                    except:
                            print '[!] Failed to remove file!'
                            count += 1
                    else:
                            print '[+] Successful removed zip file from directory'

            if count:
                    print '\n[!] Failed to remove a total of {} files '.format(count)
            else:
                    print '\n\n[+] Cleanup was successful removed all zip extenstion files from directory.'

    def _make_path(self, path, zip_file):
            """make_path(str, str) -> return(str)
            A private function that takes a two strings a
            directory path and a zip file and concatenate them to together.

            path     : The path containing the directory.
            zip_file : The zip file containing the file extenstion.
            return  : The concatenate path+zip_file string.

            >>> _make_path('/home/ab/Desktop', 'a.zip')
            /home/ab/Desktop/a.zip
            """
            return os.path.join(path, zip_file)

    def _get_all_zip_files(self):
            '''_get_all_zip_files(None) -> return(list)
            Returns a list containing zip file extenstions.
            '''
            if os.path.exists(self._directory) and os.path.isdir(self._directory):
                    os.chdir(self._directory)
                    return  glob('*.zip')
            exit('File cannot be none and it must be a directory')

    def _zip_extract(self, path, dest_dir=False):
            """_zip_extract(str, dict, str) -> return (None)
            A helper function that extracts zip files

            path         : The directory containing the zip files
            dest_dir  : Optionally path to store the extracted zip files
            Return    : None
            """
            zip_file = os.path.basename(path) # extract the basename
            try:
                    print '[-] Extracting content from zip file ({}) '.format(zip_file)
                    f = zipfile.ZipFile(path)
            except:
                    print '[!] Error failed to extract content of zip file ({})'.format(zip_file)
            else:
                    if dest_dir:
                            f.extractall(dest_dir) # store the newly files to a given directory
                            print '[+] Extracted contents from zip file ({}) and storing  it in ({}) directory'.format(zip_file, os.path.dirname(dest_dir))
                    else:
                            f.extractall()                 # store the newly extracted files to the same directory
                            print '[+] Extracted contents from zip file ({})'.format(zip_file)
            
    def extract(self, dest_dir=False):
            '''extract(optional(str)) -> return(None)
            dest_dir: Optional path to store extracted files

            Extracts all the files from a given directory.
            '''
            z_files = []    # zip files extenstion path for removal

            # extracts a single zip file
            if self._zip_file:
                    if not dest_dir:
                            dest_dir = os.path.dirname(self._zip_file)       
                    self._zip_extract(self._zip_file, dest_dir)
                    z_files.append(self._zip_file)

            # extracts all the zip files in a directory
            if self._directory:
                    zip_files = self._get_all_zip_files()

                    # extract all zip files
                    for zip_file in zip_files:
                            path = self._make_path(self._directory, zip_file) # create a path for the directory and zip file
                            self._zip_extract(path, dest_dir)                                # extract the contents of the zip
                            z_files.append(path)                                                      # append zip files for clean up
            if z_files:
                    self._clean_up(z_files) # perform clean up
            else:
                    print '[!] No zip files found.'
            
def main():

    parser = optparse.OptionParser('usage')
    parser.add_option('-d', '--directory', dest='directory', help='enter the full directory containing the zip files')
    parser.add_option('-f', '--file', dest='zip_file', help='Enter the full path of the zip file to be extracted')
    parser.add_option('-l', '--new_location', dest='new_location', help='Enter the new path for the file to be unzip')
    parser.add_option('-n', '--directory_name', dest='new_directory', help='Enter the name for the new directory')
    (options, args) = parser.parse_args()

    new_location  = False
    new_directory = False
    
    if options.directory and os.path.isdir(options.directory):
            if options.new_location and os.path.exists(options.new_location):
                 new_location = True
                 dir_path = options.new_location
            else:
                  exit('The path you entered does not exists')

             zipper = Unzip(options.directory)
            # If the user has entered the name for a new directory
            if options.new_directory:
                 new_directory = True
                 folder_path = os.path.join(dir_path, options.new_directory)

          
            if new_location and new_directory:
                zipper.extract(folder_path)
            elif new_location and not new_directory:
                  zipper.extract(new_location)

        # Write the one for the files here
        # unfinished -> including file
            
                 
                
         
    
           

if __name__ == '__main__':
    main()

                    
                
        
