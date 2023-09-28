Each task comes with a detailed description of what is expected and how it should be achieved.

Task 0: 0-body_size.sh
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the response body in bytes. The script should display only the size of the response body, nothing else.

Task 1: 1-body.sh
Write a Bash script that takes in a URL, sends a GET request to that URL, and displays the response body. The script should display only the body of the response, nothing else.

Task 2: 2-delete.sh
Write a Bash script that sends a DELETE request to a given URL and displays the response body. The script should display only the body of the response, nothing else.

Task 3: 3-methods.sh
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept for that URL.

Task 4: 4-header.sh
Write a Bash script that takes in a URL, sends a GET request to that URL, and displays the response body. The script should also send a header variable X-HolbertonSchool-User-Id with a value of 98.

Task 5: 5-post_params.sh
Write a Bash script that takes in a URL, sends a POST request to that URL, and displays the response body. The script should also set the variables email to hr@holbertonschool.com and subject to I will always be here for PLD.

Task 6: 6-peak.py
Write a function def find_peak(list_of_integers): that finds a peak in a list of unsorted integers. A peak is an element that is greater than its neighbors. For example, in the list [1, 2, 4, 6, 3], 6 is a peak. The function should return the peak element if it exists, otherwise return None. The function should have a time complexity of O(log(n)).

Task 100: 100-status_code.sh
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

Task 101: 101-post_json.sh
Write a Bash script that sends a JSON POST request to a URL passed as an argument, and displays the response body.

Task 102: 102-catch_me.sh
Write a Bash script that makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with a message containing You got me!. The response should be displayed.

Usage
The bash scripts in this repository can be run like so:

./script.sh [URL]
For example, to run the 0-body_size.sh script:

./0-body_size.sh http://example.com
Contributing
To contribute to this project, follow these steps:

Fork this repository.
Create a new branch with your feature: git checkout -b my-feature.
Commit your changes: git commit -m "feat: add new feature".
Push to the branch: git push origin my-feature.
Submit a pull request with your changes.
