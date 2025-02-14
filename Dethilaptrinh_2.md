# Bài 1: 

## Count String Permutations
Description

Find the number of strings of a given length that can be formed under the following rules:

Each letter is a vowel, that is, it is in the set{a, e, i, o, u}.
The letteramay only be followed by the letter e.
Anemay only be followed by anaor ani.
Animay not be next to anotheri.
The letteromay only be followed by anior au.
The letterumay only be followed by ana.
Example:

To illustrate some of the rules, start with the strings = 'a' and build to the right.

'a' may only be followed by 'e', so the new string can be 'ae'.
'ae' may only be followed by 'a'or 'i', so the new string can be 'aea' or 'aei'.
'aea' must be 'aeae' next, and 'aei' can be 'aeia', 'aeie', 'aeio',or 'aeiu' because an 'i'cannot follow another 'i'.
Analyses of lengths of strings up to3are in the samples below. Since the number of permutations might be very large, return the value modulo(10^9+ 7).


Input

Complete thecountPermsfunction in the editor below.

countPermshas the following parameter(s):

intn: the length of string to analyze
Constraints

0 < n < 10^5


Input Format For Custom Testing

Input from stdin will be processed as follows and passed to the function.
The only line contains an integer,n, the length of the string to analyze.



Output

Returns:

int:the number of permutations, modulo (10^9+ 7)

Sample Input 1 

STDIN     Function
-----     -----
1      →  length of string to analyze n = 1

Sample Output 1

5

Sample Input 2 

STDIN     Function
-----     -----
2      →  length of string to analyze n = 2

Sample Output 2

10

Sample Input 3 

STDIN     Function
-----     -----
3      →  length of string to analyze n = 3

Sample Output 3

19

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int countPerms(int n) {
    if (n == 0) return 0;
    
    vector<vector<long long>> dp(n + 1, vector<long long>(5, 0));
    
    
    for (int j = 0; j < 5; ++j) {
        dp[1][j] = 1;
    }
    
   
    for (int i = 2; i <= n; ++i) {
        dp[i][0] = dp[i-1][1];
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD;
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % MOD; 
        dp[i][3] = (dp[i-1][2] + dp[i-1][4]) % MOD; 
        dp[i][4] = dp[i-1][0]; 
    }
    
    
    long long result = 0;
    for (int j = 0; j < 5; ++j) {
        result = (result + dp[n][j]) % MOD;
    }
    
    return result;
}

int main() {
    int n;
    cin >> n;
    cout << countPerms(n) << endl;
    return 0;
}
```


# Bài 2

![zig-zag_array](https://github.com/user-attachments/assets/bb8b509c-94aa-464c-b0cf-b3febbd976f4)

![zig-zag2](https://github.com/user-attachments/assets/cf9987f5-ff94-485b-a167-8948ead1716d)

# Bài 3

![Screenshot 2024-12-19 111351](https://github.com/user-attachments/assets/0d9a8823-45ec-44fa-a95b-3b53863f78f4)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    long long k;
    cin >> k;

    const int MAX_OR = 1024;
    static long long prevFreq[MAX_OR], newFreq[MAX_OR], globalFreq[MAX_OR];
    for (int i = 0; i < MAX_OR; i++)
    {
        prevFreq[i] = 0;
        globalFreq[i] = 0;
    }

    for (int i = 0; i < n; i++)
    {
        for (int v = 0; v < MAX_OR; v++)
        {
            newFreq[v] = 0;
        }

        newFreq[arr[i]] += 1;

        for (int v = 0; v < MAX_OR; v++)
        {
            if (prevFreq[v] > 0)
            {
                int orVal = v | arr[i];
                newFreq[orVal] += prevFreq[v];
            }
        }

        for (int v = 0; v < MAX_OR; v++)
        {
            prevFreq[v] = newFreq[v];
            globalFreq[v] += newFreq[v];
        }
    }

    long long cumulative = 0;
    for (int v = MAX_OR - 1; v >= 0; v--)
    {
        cumulative += globalFreq[v];
        if (cumulative >= k)
        {
            cout << v << "\n";
            break;
        }
    }

    return 0;
}
```


