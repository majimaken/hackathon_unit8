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

    job_order = {'A': [ 7,  8,  5, 12, 14, 13, 15, 11,  3, 19, 16,  2, 20,  1, 17, 21,  9,  6, 10, 18,  4], 
                 'B': [35, 33, 25, 30, 22, 36, 26, 39, 34, 23, 27, 37, 28, 24, 38, 31, 32, 29], 
                 'C': [54, 43, 58, 61, 63, 41, 64, 48, 49, 56, 52, 60, 65, 45, 57, 51, 59, 44, 62, 46, 42, 53, 47, 40, 50, 55], 
                 'D': [70, 73, 66, 69, 71, 68, 67, 72]}


    # define the job order for each line
    # each job from each line has to be in the list corresponding to the line exactly once
    # # define the job order for each line
    # # each job from each line has to be in the list corresponding to the line exactly once
    # job_order = {"A": [i for i in range(1, 22)],
    #              "B": [i for i in range(22, 40)],
    #              "C": [i for i in range(40, 66)],
    #              "D": [i for i in range(66, 74)]}
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

    # submission_side_challenge = {"challenge_id": 1,  # the challenge id indicated in the documentation
    #                              "submission": "This submission is a test"  # your solution
    #                              }
    # response = requests.post('https://hackathon.unit8.com/api/submit',
    #                          headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
    #                          json=submission_side_challenge
    #                          )
    # print(response.json())
    submission_side_challenge = {"challenge_id": 6,  # the challenge id indicated in the documentation
                                 "submission": "467"  # your solution
                                 }
    response = requests.post('https://hackathon.unit8.com/api/submit',
                             headers={'Authorization': f'Token {TOKEN_ID}',
                                      'Content-Type': 'application/json'},
                             json=submission_side_challenge
                             )
    print(response.json())
