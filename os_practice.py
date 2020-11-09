import os


# print(os.getcwd())  # Current directory
# print(os.getcwdb())  # Current directory in bytes

# os.chdir('/123/123/123')  # Change directory
# print(os.getcwd())  # In directory: /123/123/123
# print(os.listdir())  # When I can go in this directory

# os.mkdir('/lala')  # Make the directory
# os.makedirs('/kiki/ki')  # Make directors

# os.rmdir('/lala')  # Remove the directory
# os.removedirs('/kiki/ki')  # Remove directors

# os.rename('test.txt', 'rename.txt')  # Rename test.txt to rename.txt

# print(os.stat('filename'))  # Statistic of file
# print(os.stat('filename').st_size)  # Show us size of file

# Like parsing and BinaryTree
"""for dir_path, directors, files in os.walk('/home/flash/Downloads'):
    print(f'Path: {dir_path}')
    print(f'Directors: {directors}')
    print(f'Files: {files}')
    print()
"""

# print(os.path.exists('/lal/fsf/adfa'))  # Was return False because this path don't real
