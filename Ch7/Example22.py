#simple regression function

cel = lam f: 5/9*(f-32)
temps = [(f,cel(f)) for f in range (0, 101, 10)]

import pandas as pd

temps_df = pd.DataFrame(temps,columns=['Fahrenheit','Celcius'])
axes = temps_df.plot(x='Fahrenheit', y='Celcius', style='--')
y_label = axes.set_ylabel('Celcius')
