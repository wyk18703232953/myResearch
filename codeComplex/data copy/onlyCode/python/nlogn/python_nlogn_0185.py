
'''
    int n;
    cin >> n;

    int sum = 0;
    map<int, int> mp;
    BigInt ans;
    for(int i = 1; i <= n; i++) {
        cin >> arr[i];
        sum += arr[i];
        
        mp[arr[i]]++;
        // fix each element as y
        ll adj = mp[arr[i]] + mp[arr[i]+1] + mp[arr[i]-1];

        ll c = sum;
        c -= mp[arr[i]]*arr[i];
        c -= mp[arr[i]+1] * (arr[i]+1);
        c -= mp[arr[i]-1] * (arr[i]-1);

        ll valid = i - adj;
        ans += ((ll)valid*(ll)arr[i])-c;
    }

    cout << ans << endl;
    '''

n = int(input())

a = map(int, input().split())
mp = {}
s = 0
ans = 0
i = 0
for x in a:
    i += 1
    s += x

    if x not in mp:
        mp[x] = 0

    if x+1 not in mp:
        mp[x+1] = 0

    if x-1 not in mp:
        mp[x-1] = 0
    mp[x] += 1

    adj = mp[x] + mp[x+1] + mp[x-1];
    c = s;
    c -= mp[x]*x;
    c -= mp[x+1] * (x+1);
    c -= mp[x-1] * (x-1);

    valid = i-adj

    ans += (valid*x)-c

print(ans)