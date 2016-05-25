#!/usr/bin/python


################################################################################
#
# Created By : Egbie Anderson Uku 
# Name Of The Program : Unzipper.Py 
# Created on the 20/05/2016 at 15:08:15 hrs
# This is version : 1 
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

    def __init__(self, path):
            self._isdir = False
            if path:
                    if os.path.isdir(path):
                            self._isdir = True
                    if self._isdir:
                            self._directory, self._file_name = path, None
                    else:
                            self._directory, self._file_name = None, path
                    
    def _clean_up(self, z_file_list):

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

    def _make_path(self, directory, zip_file):
            """make_path(str, str) -> return(str)
            Takes a two strings a directory and a file and creates a directory path
            """
            return os.path.join(directory, zip_file)

    def _get_all_zip_files(self):
            if os.path.exists(self._directory) and os.path.isdir(self._directory):
                    os.chdir(self._directory)
                    return  glob('*.zip')
            exit('File cannot be none and it must be a directory')

    def _zip_extract(self, path, dest_dir=False):
            """_zip_extract(str, dict, str) -> return (None)
            A helper function that extracts a zip file
            """
            zip_file = os.path.basename(path)
            try:
                    print '[-] Extracting content from zip file ({}) '.format(zip_file)
                    f = zipfile.ZipFile(path)
            except:
                    print '[!] Error failed to extract content of zip file ({})'.format(zip_file)
            else:
                    if dest_dir:
                            f.extractall(dest_dir)
                            print '[+] Extracted contents from zip file ({}) and storing  it in ({}) directory'.format(zip_file, os.path.dirname(dest_dir))
                    else:
                            f.extractall()
                            print '[+] Extracted contents from zip file ({})'.format(zip_file)
            
    def extract(self, dest_dir=False): 

            z_files = []              # zip files extenstion path for removal

            # extracts a single zip file
            if self._file_name:
                    if not dest_dir:
                            dest_dir = os.path.dirname(self._file_name)       
                    self._zip_extract(self._file_name, dest_dir)
                    z_files.append(self._file_name)

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
    parser.add_option('-d', '--directory', dest='directory', help='enter the directory or file path')
    parser.add_option('-n', '--new_location', dest='new_location', help='Enter the new path for the file to be unzip')
    parser.add_option('-c', '--create_directory', dest='new_directory', help='Enter the name for the new directory')
    (options, args) = parser.parse_args()

    if options.directory and os.path.isdir(options.directory):
            if not options.new_location and options.new_directory:
                    path = os.path.join(path, dir_name)
            if options.new_directory:
                    make_directory(options.new_directory, options.directory)





if __name__ == '__main__':
    main()

                    
                
        
