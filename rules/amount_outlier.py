import statistics

def check(tx, history):
    amounts = [t['amount'] for t in history if t['client_id'] == tx['client_id']]
    if len(amounts) < 10: return {'triggered': False}
    m, s = statistics.mean(amounts), statistics.stdev(amounts)
    return {'triggered': tx['amount'] > m + 3*s, 'reason': 'outlier'}
