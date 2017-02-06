import re

def divide(dividend, divisor):
    sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
    a, b = abs(dividend), abs(divisor)
    ret, c = 0, 0

    while a >= b:
        c = b
        i = 0
        while a >= c:
            a -= c
            ret += (1 << i)
            i += 1
            c <<= 1

    if sign:
        ret = -ret
    return min(max(-2147483648, ret), 2147483647)

def createOrcSql(fid, tableid, colname, coltype, cnname,):
    BASE_SQL = "insert into TBDL_META_FIELD (FID,TABLEID,COLNAME,COLTYPE,COLCNNAME,COLREMARK,FCREATETIME) VALUES (" + \
               "{FID},{TABLEID},{COLNAME},{COLTYPE},{COLCNNAME},'','');"
    sql = BASE_SQL.format(FID=fid,TABLEID=tableid,COLNAME=colname,COLTYPE=coltype,COLCNNAME=cnname)
    print(sql)

if __name__ == '__main__':
    with open('names.txt','r') as f:
        p = re.compile(r' +')
        w = "'%s'"
        for linenum, line in enumerate(f.readlines()):
            l = p.sub(" ",line.strip()).split(" ")
            createOrcSql(linenum+24, 3, w%l[0], w%l[1], w%l[2])
