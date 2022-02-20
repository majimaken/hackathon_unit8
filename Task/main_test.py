import requests
import pandas as pd
import json
from pandas import json_normalize

# Replace this with your token (available on hackathon.unit8.com, after logging in)
# If your request returns {'detail': 'Invalid token.'} then you did not correctly set this variable
TOKEN_ID = 'fed877446aa8e41f956b19f86383d493a7a001a1'


if __name__ == '__main__':
    ####################################################
    # ----- EXAMPLE OF MAIN CHALLENGE SUBMISSION ----- #
    ####################################################
    #
    # job_order = {'A': [ 7,  8,  5, 12, 14, 13, 15, 11,  3, 19, 16,  2, 20,  1, 17, 21,  9,  6, 10, 18,  4],
    #              'B': [35, 33, 25, 30, 22, 36, 26, 39, 34, 23, 27, 37, 28, 24, 38, 31, 32, 29],
    #              'C': [54, 43, 58, 61, 63, 41, 64, 48, 49, 56, 52, 60, 65, 45, 57, 51, 59, 44, 62, 46, 42, 53, 47, 40, 50, 55],
    #              'D': [70, 73, 66, 69, 71, 68, 67, 72]}

    # define the job order for each line
    # each job from each line has to be in the list corresponding to the line exactly once
    # # define the job order for each line
    # # each job from each line has to be in the list corresponding to the line exactly once
    # job_order = {"A": [i for i in range(1, 22)],
    #              "B": [i for i in range(22, 40)],
    #              "C": [i for i in range(40, 66)],
    #              "D": [i for i in range(66, 74)]}
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
    # # print(response.text)
    # response = response.json()
    # print(response)

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
    # resource retrieval needs to follow the format dict("challenge_id": integer)
    # submission_side_challenge = {"challenge_id": 3}  # the challenge id indicated in the documentation
    # response = requests.get('https://hackathon.unit8.com/api/get_resource',
    #                         headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
    #                         json=submission_side_challenge
    #                         )
    # print(response.json())
    
    # dic = response.json()
    # info = json.loads(dic)
    
    # dat_3 = pd.read_json(dic, orient = "columns")
    
    # df = pd.DataFrame.from_dict({(i,j): info[i][j] 
    #                        for i in info.keys() 
    #                        for j in info[i].keys()},
    #                    orient='index')
    

    # ####################################################
    # # ----- EXAMPLE OF SIDE CHALLENGE SUBMISSION ----- #
    # ####################################################

    # submission_side_challenge = {"challenge_id": 3,  # the challenge id indicated in the documentation
    #                              "submission": "feature_35"  # your solution
    #                              }
    # response = requests.post('https://hackathon.unit8.com/api/submit',
    #                          headers={'Authorization': f'Token {TOKEN_ID}',
    #                                   'Content-Type': 'application/json'},
    #                          json=submission_side_challenge
    #                          )
    # print(response.json())
    #
    # response = requests.post(
    #     'https://hackathon.unit8.com/api/submit',
    #     headers={'Authorization': 'Token fed877446aa8e41f956b19f86383d493a7a001a1'},
    #     json={'challenge_id': 3, 'submission': "feature_36"}
    # )
    # print(response.json())

    # submission_side_challenge = {"challenge_id": 4,  # the challenge id indicated in the documentation
    #                               "submission": "8"  # your solution
    #                               }
    response = requests.post(
                            'https://hackathon.unit8.com/api/submit',
                                headers={'Authorization': 'Token fed877446aa8e41f956b19f86383d493a7a001a1'},
                                json={'challenge_id': 2, 'submission': {126: 1.0,
                                 1144: 0.0,
                                 764: 1.0,
                                 103: 0.0,
                                 930: 1.0,
                                 720: 1.0,
                                 304: 0.0,
                                 1115: 1.0,
                                 2: 1.0,
                                 167: 0.0,
                                 295: 0.0,
                                 1004: 0.0,
                                 664: 0.0,
                                 350: 1.0,
                                 784: 1.0,
                                 941: 1.0,
                                 581: 0.0,
                                 604: 1.0,
                                 780: 1.0,
                                 519: 0.0,
                                 79: 1.0,
                                 1059: 1.0,
                                 1073: 0.0,
                                 1097: 1.0,
                                 346: 0.0,
                                 226: 1.0,
                                 991: 0.0,
                                 747: 0.0,
                                 958: 0.0,
                                 965: 1.0,
                                 420: 1.0,
                                 116: 0.0,
                                 1128: 0.0,
                                 733: 0.0,
                                 68: 1.0,
                                 204: 0.0,
                                 157: 1.0,
                                 605: 0.0,
                                 657: 0.0,
                                 557: 0.0,
                                 265: 0.0,
                                 301: 1.0,
                                 115: 0.0,
                                 666: 0.0,
                                 1015: 1.0,
                                 206: 0.0,
                                 775: 1.0,
                                 637: 1.0,
                                 729: 1.0,
                                 967: 1.0,
                                 1069: 0.0,
                                 789: 0.0,
                                 695: 0.0,
                                 788: 1.0,
                                 585: 1.0,
                                 189: 1.0,
                                 269: 0.0,
                                 950: 1.0,
                                 737: 0.0,
                                 396: 0.0,
                                 365: 0.0,
                                 361: 0.0,
                                 749: 0.0,
                                 466: 0.0,
                                 730: 1.0,
                                 708: 1.0,
                                 857: 1.0,
                                 74: 1.0,
                                 100: 1.0,
                                 279: 1.0,
                                 28: 0.0,
                                 341: 1.0,
                                 921: 0.0,
                                 710: 0.0,
                                 242: 1.0,
                                 667: 0.0,
                                 312: 1.0,
                                 1002: 0.0,
                                 1078: 0.0,
                                 846: 1.0,
                                 169: 0.0,
                                 318: 1.0,
                                 470: 1.0,
                                 403: 1.0,
                                 867: 0.0,
                                 240: 0.0,
                                 1072: 1.0,
                                 1103: 0.0,
                                 963: 1.0,
                                 932: 1.0,
                                 45: 1.0,
                                 549: 1.0,
                                 317: 1.0,
                                 1003: 0.0,
                                 572: 1.0,
                                 1018: 0.0,
                                 16: 1.0,
                                 1117: 0.0,
                                 792: 1.0,
                                 717: 0.0,
                                 65: 1.0,
                                 1147: 0.0,
                                 130: 1.0,
                                 106: 1.0,
                                 931: 0.0,
                                 511: 1.0,
                                 803: 0.0,
                                 459: 1.0,
                                 175: 0.0,
                                 225: 1.0,
                                 879: 0.0,
                                 352: 1.0,
                                 1022: 0.0,
                                 734: 1.0,
                                 502: 1.0,
                                 611: 0.0,
                                 447: 1.0,
                                 1044: 0.0,
                                 1053: 1.0,
                                 949: 1.0,
                                 592: 0.0,
                                 464: 1.0,
                                 238: 0.0,
                                 839: 0.0,
                                 294: 1.0,
                                 1: 1.0,
                                 123: 0.0,
                                 129: 1.0,
                                 207: 0.0,
                                 699: 1.0,
                                 833: 0.0,
                                 112: 0.0,
                                 192: 0.0,
                                 202: 1.0,
                                 122: 1.0,
                                 322: 1.0,
                                 34: 0.0,
                                 685: 0.0,
                                 77: 0.0,
                                 577: 0.0,
                                 650: 1.0,
                                 738: 1.0,
                                 751: 0.0,
                                 518: 0.0,
                                 231: 0.0,
                                 473: 0.0,
                                 1121: 1.0,
                                 552: 1.0,
                                 781: 1.0,
                                 418: 0.0,
                                 425: 0.0,
                                 214: 0.0,
                                 758: 0.0,
                                 741: 1.0,
                                 936: 0.0,
                                 314: 1.0,
                                 889: 1.0,
                                 1126: 0.0,
                                 1108: 1.0,
                                 680: 0.0,
                                 998: 1.0,
                                 630: 1.0,
                                 508: 1.0,
                                 1014: 0.0,
                                 239: 1.0,
                                 353: 0.0,
                                 1089: 0.0,
                                 640: 1.0,
                                 1031: 0.0,
                                 1138: 0.0,
                                 467: 0.0,
                                 556: 1.0,
                                 489: 0.0,
                                 429: 1.0,
                                 457: 0.0,
                                 533: 0.0,
                                 977: 1.0,
                                 285: 0.0,
                                 1047: 1.0,
                                 914: 1.0,
                                 1112: 1.0,
                                 899: 0.0,
                                 139: 0.0,
                                 787: 0.0,
                                 1093: 0.0,
                                 773: 1.0,
                                 601: 0.0,
                                 831: 0.0,
                                 674: 1.0,
                                 373: 0.0,
                                 952: 1.0,
                                 677: 0.0,
                                 422: 0.0,
                                 311: 1.0,
                                 47: 0.0,
                                 356: 1.0,
                                 424: 1.0,
                                 856: 1.0,
                                 44: 0.0,
                                 863: 0.0,
                                 719: 0.0,
                                 379: 0.0,
                                 54: 1.0,
                                 1029: 1.0,
                                 686: 1.0,
                                 1081: 0.0,
                                 409: 1.0,
                                 1133: 1.0,
                                 913: 0.0,
                                 355: 0.0,
                                 412: 0.0,
                                 537: 1.0,
                                 132: 0.0,
                                 683: 0.0,
                                 1058: 1.0,
                                 121: 0.0,
                                 1063: 0.0,
                                 598: 0.0,
                                 968: 0.0,
                                 582: 0.0,
                                 837: 0.0,
                                 334: 0.0,
                                 398: 1.0,
                                 777: 0.0,
                                 237: 1.0,
                                 883: 0.0,
                                 917: 0.0,
                                 855: 0.0,
                                 119: 0.0,
                                 903: 0.0}}
                                ) 
    print(response.json())
