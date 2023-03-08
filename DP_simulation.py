import random
import pandas as pd
import numpy as np

DP_results = pd.DataFrame({"DP":[]})
for i in range (1, 1001):
    DP = 1
    count = 0
    while True:
        '''
        #最小サイズ一定
        ELONGATION_RATE = 50
        DEGRADATION_RATE = 1
        FINISH_RATE = 1
        max_DP = 10000
        min_DP = 0
        '''

        '''
        #最小サイズ揺らぎ
        ELONGATION_RATE = 45
        DEGRADATION_RATE = 40
        FINISH_RATE = 10
        min_DP = np.random.normal(20)
        '''

        '''
        #DPによって異なる反応速度
        ELONGATION_RATE = int(100000 * 3 / (4 * 3.14 * DP ** 3))
        DEGRADATION_RATE = int(100000 * 3 / (4 * 3.14 * (40 - DP) ** 3))
        FINISH_RATE = int(1000 * 3 / (4 * 3.14 * (20 - DP) ** 3)) if DP < 20 else int(1000 * 3 / (4 * 3.14 * (DP - 19) ** 3))
        min_DP = 0
        max_DP = 10000
        '''

        '''
        #DPによって異なる反応速度2
        ELONGATION_RATE = 40 - DP
        DEGRADATION_RATE = DP
        FINISH_RATE = 1 + DP if DP < 20 else 41 - DP
        min_DP = 0
        '''

        '''
        #最小サイズ揺らぎ＋DPによって異なる反応速度
        ELONGATION_RATE = int(55000 * 3 / (4 * 3.14 * DP ** 3))
        DEGRADATION_RATE = int(3 / (4 * 3.14 * (40 - DP) ** 3))
        FINISH_RATE = 1
        min_DP = np.random.normal(20)
        '''

        '''
        #最大サイズ揺らぎ
        ELONGATION_RATE = 40
        DEGRADATION_RATE = 1
        FINISH_RATE = 1
        min_DP = 0
        max_DP = np.random.normal(20)
        '''

        
        #急激伸長→じわじわ伸長
        threshold = np.random.normal(17)
        if DP < threshold: ELONGATION_RATE = 40
        else: ELONGATION_RATE = round(40 / DP)
        DEGRADATION_RATE = 1
        FINISH_RATE = 1
        min_DP = 0 #np.random.normal(14)
        max_DP = 10000
        

        RATE = ["E"] * ELONGATION_RATE + ["D"] * DEGRADATION_RATE + ["C"] * FINISH_RATE
        reaction = random.choice(RATE)

        if reaction == "E" and DP < max_DP:
            DP += 1
        elif reaction == "D":
            if DP > 1:
                DP -= 1
            else:
                pass
        elif reaction == "C" and DP >= min_DP:
            break

        count += 1
        if count == 100:
            break
        
    DP_results.loc[i] = DP

DP_count = DP_results.groupby("DP").size()
ax = DP_count.plot.bar(rot = 0)
fig = ax.get_figure()
fig.show()
