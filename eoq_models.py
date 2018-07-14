import numpy as np
from dataclasses import dataclass
@dataclass
class EOQResult:
    model:str; Q:float; orders:float; order_cost:float; hold_cost:float; total:float; cycle_days:float
def classic_eoq(D,S,H):
    q=np.sqrt(2*D*S/H); n=D/q
    return EOQResult("Classic EOQ",round(q,2),round(n,2),round(n*S,2),round(q/2*H,2),round(n*S+q/2*H,2),round(365/n,1))
def eoq_shortage(D,S,H,B):
    q=np.sqrt(2*D*S/H)*np.sqrt((H+B)/B); n=D/q
    return EOQResult("EOQ+Shortage",round(q,2),round(n,2),round(n*S,2),round(q/2*H,2),round(n*S+q/2*H,2),round(365/n,1))
def rop(d_day,lt,std,sl=0.95):
    from scipy.stats import norm; z=norm.ppf(sl); ss=z*std*np.sqrt(lt)
    return {"rop":round(d_day*lt+ss,2),"safety_stock":round(ss,2)}
if __name__=="__main__":
    r=classic_eoq(10000,50,2); print(f"EOQ={r.Q}, Cost=${r.total:,.2f}, Cycle={r.cycle_days}d")
