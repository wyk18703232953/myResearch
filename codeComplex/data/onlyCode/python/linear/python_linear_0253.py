def getIntList():
    return list(map(int, input().split()));
nbColumn, h=getIntList();
if (nbColumn-2)*2<h:
    print('NO')
else:
    print('YES')
    if h%2==0:
        print('.'*nbColumn);
        print('.'+'#'*(h//2)+'.'*(nbColumn-1-h//2));
        print('.'+'#'*(h//2)+'.'*(nbColumn-1-h//2));
        print('.'*nbColumn);
    else:
        print('.'*nbColumn);
        hFirst=min(h, nbColumn-2);
        countPoint=(nbColumn-hFirst)//2;
        print('.'*countPoint+'#'*hFirst+'.'*countPoint);
        hSecond=(h-hFirst)//2;
        countPoint=nbColumn-2*hSecond-2;
        print('.'+'#'*hSecond+'.'*countPoint+'#'*hSecond+'.');
        print('.'*nbColumn);   