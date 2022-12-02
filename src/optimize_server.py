import sys
import json
import subprocess

import logger

def _decode_response(response):
  decoded_response = json.loads(response)
  return float(decoded_response['score'])

def _request_score_list(solution_list, match_number):
  score_list = []
  proc_list = []
  for solution in solution_list:
    command = f'echo {solution} | opt submit --match={match_number}'
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  shell=True)
    proc_list.append(proc)

  for proc in proc_list:
    try:
      response = proc.communicate()[0]
      score = _decode_response(response)
      score_list.append(score)
    except:
      logger.log_warn('submit fail!')
      score_list.append(sys.maxsize)
  return score_list

def optimize(solution_list, match_number):
  score_list = _request_score_list(solution_list, match_number)
  return score_list
