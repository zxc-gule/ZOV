import Libsort
import time
Massiv = [random.randint(1,100000) for i in range(N)]
Start = time.time()
Libsort.insertion_sort(Massiv)
Finish = time.time()
Res_msec = (Finish – Start)*1000
