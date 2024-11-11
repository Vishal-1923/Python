# ****************************************** Multi Processing **************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/98-Day-98-MultiProcessing-in-Python/.tutorial/01-MultiProcessing.md

# sometimes we want to run multiple processes using our 1 program i.e., python program will spawn variuos child processes. (spawn: process ko start krna)

# if u have multiple cpus then u can use them via multiple processes.
# spawning a thread is easy, takes less time and r light weight, they r part of process.

# multi-processing: jb aap multiple heavy task concurrently perform krna chaho to kr skte ho use

# done via importing multiprocessing module in python

import multiprocessing

import concurrent.futures
import requests

# to download a img
def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"

# normal way
# for i in range(5):
#     downloadFile(url, i)



# multi-processing way
# pros = []
# for i in range(5):
#   p = multiprocessing.Process(target=downloadFile, args=[url, i])
#   p.start()
#   pros.append(p)

# for p in pros:
#   p.join()

# concurrent_features way
with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(6)]
  l2 = [i for i in range(6)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)

