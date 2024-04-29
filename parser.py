import re

def parse_html_file(file_path):
    with open(f'{file_path}.html', 'r') as file:
        html_content = file.read()

    urls = re.findall(r'instagram\.com/[\w/]+', html_content)

    with open(f'{file_path}.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = set(f1.readlines())
        lines2 = set(f2.readlines())

    unique_lines = lines1.difference(lines2)

    return unique_lines

if __name__ == '__main__':
    parse_html_file('followers_1')
    parse_html_file('following')
    
    non_mutual_followers = compare_files('followers_1.txt', 'following.txt')
    for line in non_mutual_followers:
        print(line.strip())

    print('---\n\n')

    non_mutual_following = compare_files('following.txt', 'followers_1.txt')
    for line in non_mutual_following:
        print(line.strip())