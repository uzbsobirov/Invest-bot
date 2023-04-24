def input_sum(item):
    if item is None:
        name = "<code>Kiritilmagan</code>"
        return name
    else:
        name = item
        return name

def crypto(item):
    if item is None:
        name = "<code>Kiritilmagan</code>"
        return name
    else:
        name = item
        return name

def percent(item):
    if item is None:
        name = "<code>Kiritilmagan</code>"
        return name
    else:
        name = item
        return name

def detect_crypto(crypto):
    if crypto == 'premiumbtc':
        return '🟢Premium 3.4%'

    elif crypto == 'standarteth':
        return '🔵Standard  2.3%'

    elif crypto == 'maximumltc':
        return '🟡 Maximum 1,8%'

    else:
        pass

def detect_percent(crypto):
    if crypto == 'premiumbtc':
        return 3.4

    elif crypto == 'standarteth':
        return 2.3

    else:
        return 1.8