from multiprocessing import Pool


def mp_map(func, data, workers=4):
with Pool(processes=workers) as pool:
return pool.map(func, data)
