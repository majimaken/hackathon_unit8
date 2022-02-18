import requests
import pandas as pd
import json

# Replace this with your token (available on hackathon.unit8.com, after logging in)
# If your request returns {'detail': 'Invalid token.'} then you did not correctly set this variable
TOKEN_ID = 'fed877446aa8e41f956b19f86383d493a7a001a1'


if __name__ == '__main__':
    ####################################################
    # ----- EXAMPLE OF MAIN CHALLENGE SUBMISSION ----- #
    ####################################################

<<<<<<< Updated upstream
    job_order = {'A': [11,12,14,17,18,19,20,21,1,2,3,4,5,6,7,8,9,10,13,15,16], 
                 'B': [33, 23, 29, 39, 24, 34, 28, 38, 32, 22, 25, 26, 37, 30, 35, 31, 27, 36], 
                 'C': [65, 64, 59, 43, 57, 61, 52, 41, 48, 56, 54, 55, 46, 44, 62, 47, 45, 49, 53, 50, 63, 51, 42, 40, 58, 60], 
                 'D': [70, 72, 66, 67, 71, 68, 73, 69]}


    # define the job order for each line
    # each job from each line has to be in the list corresponding to the line exactly once
=======
    # # define the job order for each line
    # # each job from each line has to be in the list corresponding to the line exactly once
>>>>>>> Stashed changes
    # job_order = {"A": [i for i in range(1, 22)],
    #              "B": [i for i in range(22, 40)],
    #              "C": [i for i in range(40, 66)],
    #              "D": [i for i in range(66, 74)]}
<<<<<<< Updated upstream
    # submission has to have the format dict("job_order": dict(string_keys: list of integers))
    submission = {"job_order": job_order}

    """
    call the API and get back a requests.models.Response object consisting of:
        - submission_id
        - avg_score: an average of the processing time of the four lines
        - score_line_A: the processing time of line A
        - score_line_B: the processing time of line B
        - score_line_C: the processing time of line C
        - score_line_D: the processing time of line D
        - log: a log file containing all information of the processing of all modules (as dictionary (!))
    """
    response = requests.post('https://hackathon.unit8.com/api/submit',
                             headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
                             json=submission
                             )

    # convert the response object to a dictionary for further processing
    print(response.text)
    response = response.json()
    print(response)

    # ############################################################
    # # ----- EXAMPLE OF SIDE CHALLENGE RESOURCE RETRIEVAL ----- #
    # ############################################################

=======
    # # submission has to have the format dict("job_order": dict(string_keys: list of integers))
    # submission = {"job_order": job_order}
    #
    # """
    # call the API and get back a requests.models.Response object consisting of:
    #     - submission_id
    #     - avg_score: an average of the processing time of the four lines
    #     - score_line_A: the processing time of line A
    #     - score_line_B: the processing time of line B
    #     - score_line_C: the processing time of line C
    #     - score_line_D: the processing time of line D
    #     - log: a log file containing all information of the processing of all modules (as dictionary (!))
    # """
    # response = requests.post('https://hackathon.unit8.com/api/submit',
    #                          headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
    #                          json=submission
    #                          )
    #
    # # convert the response object to a dictionary for further processing
    # print(response.text)
    # response = response.json()
    # print(response)
    #
    # ############################################################
    # # ----- EXAMPLE OF SIDE CHALLENGE RESOURCE RETRIEVAL ----- #
    # ############################################################
    #
>>>>>>> Stashed changes
    # # resource retrieval needs to follow the format dict("challenge_id": integer)
    # submission_side_challenge = {"challenge_id": 1}  # the challenge id indicated in the documentation
    # response = requests.get('https://hackathon.unit8.com/api/get_resource',
    #                         headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
    #                         json=submission_side_challenge
    #                         )
    # print(response.json())

    # ####################################################
    # # ----- EXAMPLE OF SIDE CHALLENGE SUBMISSION ----- #
    # ####################################################

<<<<<<< Updated upstream
    # submission_side_challenge = {"challenge_id": 1,  # the challenge id indicated in the documentation
    #                              "submission": "This submission is a test"  # your solution
    #                              }
    # response = requests.post('https://hackathon.unit8.com/api/submit',
    #                          headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
    #                          json=submission_side_challenge
    #                          )
    # print(response.json())
=======
    submission_side_challenge = {"challenge_id": 6,  # the challenge id indicated in the documentation
                                 "submission": "467"  # your solution
                                 }
    response = requests.post('https://hackathon.unit8.com/api/submit',
                             headers={'Authorization': f'Token {TOKEN_ID}',
                                      'Content-Type': 'application/json'},
                             json=submission_side_challenge
                             )
    print(response.json())
>>>>>>> Stashed changes
