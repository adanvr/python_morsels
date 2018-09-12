#>>> get_earliest("01/27/1832", "01/27/1756")
#"01/27/1756"
#>>> get_earliest("02/29/1972", "12/21/1946")
#"12/21/1946"
# 
# >>> get_earliest("02/24/1946", "03/21/1946")
#"02/24/1946"
#>>> get_earliest("06/21/1958", "06/24/1958")
#"06/21/1958"
import datetime as dt

#def get_earliest(date_1, date_2):
#    m1, d1, y1 = date_1.split('/')
#    m2, d2, y2 = date_2.split('/')
#    if (y1, m1, d1) < (y2, m2, d2):
#        return date_1
#    else:
#        return date_2


def get_earliest(*dates):
    """Return earliest of given MM/DD/YYYY-formatted date strings."""
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)